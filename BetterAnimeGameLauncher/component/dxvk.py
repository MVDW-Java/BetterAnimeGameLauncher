from BetterAnimeGameLauncher import *

from BetterAnimeGameLauncher.util.cache import saveCache
from BetterAnimeGameLauncher.util.config import saveConfig

import os
import sys
import requests
import tarfile
import io
import shutil
import hashlib

def initDXVK(val):
    # Check if given DXVK type/version exist
    if(val != None):
        checkDXVK(val)

    # Create cache for installed data when needed
    if "INSTALLED" not in CACHE:
        CACHE["INSTALLED"] = {};

    # Set DXVK version into config
    if "DXVK" not in CONFIG:
        if(val == None):
            CONFIG["DXVK"] = METADATA["dxvk"]["DEFAULT"]
        else:
            CONFIG["DXVK"] = val; 

    # Check if DXVK installation exist in the cache 
    if "DXVK" not in CACHE["INSTALLED"]:
        CACHE["INSTALLED"]["DXVK"] = []


    dxvk_path = os.path.join(PATH_DATA_DXVK_DIR, CONFIG["DXVK"])

    if CONFIG["DXVK"] not in CACHE["INSTALLED"]["DXVK"]:
        CACHE["INSTALLED"]["DXVK"].append(CONFIG["DXVK"])

    if not os.path.exists(dxvk_path):
        downloadDXVK(CONFIG["DXVK"])

    dxvk_x32 = os.path.join(dxvk_path, "x32")
    dxvk_x64 = os.path.join(dxvk_path, "x64")

    win_32 = os.path.join(PATH_DATA_PREFIX_DIR, "drive_c", "windows", "system32")
    win_64 = os.path.join(PATH_DATA_PREFIX_DIR, "drive_c", "windows", "syswow64")

    # check if DXVK is installed
    for file in os.listdir(dxvk_x32):
        # DXVK x32 -> syswow64
        dxvk32_filepath = os.path.join(dxvk_x32, file);
        dxvk32_hash = hashlib.md5(open(dxvk32_filepath,'rb').read()).hexdigest()

        win64_filepath = os.path.join(win_64, file);
        win64_hash =  hashlib.md5(open(win64_filepath,'rb').read()).hexdigest()
        
        # DXVK x64 -> system32
        dxvk64_filepath = os.path.join(dxvk_x64, file);
        dxvk64_hash = hashlib.md5(open(dxvk64_filepath,'rb').read()).hexdigest()

        win32_filepath = os.path.join(win_32, file);
        win32_hash =  hashlib.md5(open(win32_filepath,'rb').read()).hexdigest()

        # replace x32 files
        if(win64_hash != dxvk32_hash):
            print("replace x32 files")
            os.remove(win64_filepath)
            shutil.copyfile(dxvk32_filepath, win64_filepath)

        # replace x64 files
        if(win32_hash != dxvk64_hash):
            print("replace x64 files")
            os.remove(win32_filepath)
            shutil.copyfile(dxvk64_filepath, win32_filepath)


    # Save changed data
    saveCache()
    saveConfig()


def verDXVK(dxvk):
    dxvk_split = dxvk.split("_");

    # Check dxvk argument
    if len(dxvk_split) != 2:
        print(f"error: given DXVK format is invalid")
        sys.exit(1)

    # return dxvk type and version
    return dxvk_split[0], dxvk_split[1]

def checkDXVK(dxvk):

    dxvk_type, dxvk_ver = verDXVK(dxvk)

    # Check dxvk type
    if dxvk_type not in METADATA["dxvk"]["TYPES"]:
        print(f"error: the DXVK type '{dxvk_type}' does not exist")
        sys.exit(1)

    # Check if given metadata is correct
    if (dxvk_type not in METADATA["dxvk"]["DATA"]) or ("VERSIONS" not in METADATA["dxvk"]["DATA"][dxvk_type]):
        print(f"error: given data from server does not have the correct format for DXVK type '{dxvk_type}'")
        sys.exit(1)

    # check DXVK ver
    for key in METADATA["dxvk"]["DATA"][dxvk_type]["VERSIONS"]:
        if dxvk_ver == key["VERSION"]:
            return;

    # if DXVK version is invalid exit
    print(f"error: the dxvk version '{dxvk_ver}' does not exist")
    sys.exit(1)


def downloadDXVK(dxvk):
    dxvk_type, dxvk_ver = verDXVK(dxvk)
    dxvk_url = None

    for key in METADATA["dxvk"]["DATA"][dxvk_type]["VERSIONS"]:
        if dxvk_ver == key["VERSION"]:
            dxvk_url = key["URL"]
    if dxvk_url is None:
        print(f"error: the DXVK url does not exist")
        sys.exit(1)

    if not os.path.exists(PATH_DATA_DXVK_DIR):
        os.makedirs(PATH_DATA_DXVK_DIR)

    response = requests.get(dxvk_url, stream=True)
    file_type = None

    # Check file format
    if dxvk_url.endswith('.tar.xz'):
        file_type = "xz"
    elif dxvk_url.endswith('.tar.gz'):
        file_type = "gz"

    # exit when the file type is invalid
    if file_type == None:
        print("error: Recieved an unexpected archive type when trying to download DXVK.")
        sys.exit(1)



    # Create a temporary directory to extract the tar file
    temp_dir = os.path.join(PATH_DATA_DXVK_DIR, 'temp_extracted')
    os.makedirs(temp_dir, exist_ok=True)

    try:
        file = tarfile.open(fileobj=response.raw, mode=f"r|{file_type}")
        file.extractall(temp_dir)
        
        # Get the list of items in the temporary directory
        items = os.listdir(temp_dir)
        if len(items) != 1 or not os.path.isdir(os.path.join(temp_dir, items[0])):
            print("error: Unexpected structure in the tar file.")
            sys.exit(1)
        
        # Rename the first folder to the DXVK name
        source_path = os.path.join(temp_dir, items[0])
        destination_path = os.path.join(PATH_DATA_DXVK_DIR, dxvk)
        os.rename(source_path, destination_path)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
        