from BetterAnimeGameLauncher import *

from BetterAnimeGameLauncher.util.cache import saveCache
from BetterAnimeGameLauncher.util.config import saveConfig

import os
import sys
import requests
import tarfile
import io
import shutil


def initWine(val):
    # Check if given wine type/version exist
    if(val != None):
        checkWine(val)

    # Create cache for installed data when needed
    if "INSTALLED" not in CACHE:
        CACHE["INSTALLED"] = {};

    # Check if installed type exist in the cache 
    if "INSTALLED" not in CACHE:
        CACHE["INSTALLED"] = {}

    # Set wine version into config
    if "WINE" not in CONFIG:
        if(val == None):
            CONFIG["WINE"] = METADATA["wine"]["DEFAULT"]
        else:
            CONFIG["WINE"] = val; 

    # Check if wine installation exist in the cache 
    if "WINE" not in CACHE["INSTALLED"]:
        CACHE["INSTALLED"]["WINE"] = []


    if CONFIG["WINE"] not in CACHE["INSTALLED"]["WINE"]:
        downloadWine(CONFIG["WINE"])
        CACHE["INSTALLED"]["WINE"].append(CONFIG["WINE"])

    # Save changed data
    saveCache()
    saveConfig()


def wineVer(wine):
    wine_split = wine.split("_");

    # Check wine argument
    if len(wine_split) != 2:
        print(f"error: given wine format is invalid")
        sys.exit(1)

    # return wine type and version
    return wine_split[0], wine_split[1]

# Checking if the given wine parameter is valid and exist
def checkWine(wine):

    wine_type, wine_ver = wineVer(wine)

    # Check wine type
    if wine_type not in METADATA["wine"]["TYPES"]:
        print(f"error: the wine type '{wine_type}' does not exist")
        sys.exit(1)

    # Check if given metadata is correct
    if (wine_type not in METADATA["wine"]["DATA"]) or ("VERSIONS" not in METADATA["wine"]["DATA"][wine_type]):
        print(f"error: given data from server does not have the correct format for wine type '{wine_type}'")
        sys.exit(1)

    # check wine ver
    for key in METADATA["wine"]["DATA"][wine_type]["VERSIONS"]:
        if wine_ver == key["VERSION"]:
            return;

    # if wine version is invalid exit
    print(f"error: the wine version '{wine_ver}' does not exist")
    sys.exit(1)




def downloadWine(wine):
    wine_type, wine_ver = wineVer(wine)
    wine_url = None

    for key in METADATA["wine"]["DATA"][wine_type]["VERSIONS"]:
        if wine_ver == key["VERSION"]:
            wine_url = key["URL"]
    if wine_url is None:
        print(f"error: the wine url does not exist")
        sys.exit(1)

    if not os.path.exists(PATH_DATA_WINE_DIR):
        os.makedirs(PATH_DATA_WINE_DIR)

    response = requests.get(wine_url, stream=True)

    # Create a temporary directory to extract the tar file
    temp_dir = os.path.join(PATH_DATA_WINE_DIR, 'temp_extracted')
    os.makedirs(temp_dir, exist_ok=True)

    try:
        file = tarfile.open(fileobj=response.raw, mode="r|xz")
        file.extractall(temp_dir)
        
        # Get the list of items in the temporary directory
        items = os.listdir(temp_dir)
        if len(items) != 1 or not os.path.isdir(os.path.join(temp_dir, items[0])):
            print("error: Unexpected structure in the tar file.")
            sys.exit(1)
        
        # Rename the first folder to the wine name
        source_path = os.path.join(temp_dir, items[0])
        destination_path = os.path.join(PATH_DATA_WINE_DIR, wine)
        os.rename(source_path, destination_path)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
