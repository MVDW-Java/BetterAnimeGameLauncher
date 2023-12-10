from BetterAnimeGameLauncher import *

from BetterAnimeGameLauncher.util.download import download_file
from BetterAnimeGameLauncher.util.cache import saveCache
from BetterAnimeGameLauncher.util.config import saveConfig

import os
import base64
import requests
import json
import hashlib
import zipfile


# Lauch game
def launchGenshin():
    # check config
    if CONFIG["installed_genshin_ver"] is None:
        CONFIG["installed_genshin_ver"] = "0.0.0"
    if CONFIG["lang"] is None:
        CONFIG["lang"] = ["en-us"]

    api = base64.b64decode("aHR0cHM6Ly9zZGstb3Mtc3RhdGljLmhveW92ZXJzZS5jb20vaGs0ZV9nbG9iYWwvbWRrL2xhdW5jaGVyL2FwaS9yZXNvdXJjZT9rZXk9Z2NTdGdhcmgmbGF1bmNoZXJfaWQ9MTA=")
    api_responce = json.loads(requests.get(api).content)

    # basic game info
    game_version = api_responce["data"]["game"]["latest"]["version"]
    game_executable = api_responce["data"]["game"]["latest"]["entry"]

    if (CONFIG["installed_genshin_ver"] != game_version) or not os.path.exists(PATH_DATA_GAME_GENSHIN_DIR):
        print("Installing Genshin Impact...")
        installGenshin(api_responce)
        saveCache()
        saveConfig()

    game_path = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, game_executable)

    wine_bin = os.path.join(PATH_DATA_WINE_DIR, CONFIG["WINE"], "bin", "wine")
    wine_exec = f"WINEPREFIX=\"{PATH_DATA_PREFIX_DIR}\" WINEDLLOVERRIDES=\"d3d11,d3d10core,dxgi,d3d9=n\" {wine_bin} {game_path}" #


    os.chdir(PATH_DATA_GAME_GENSHIN_DIR)
    os.system(wine_exec)
    
    
# Install game
def installGenshin(api_responce):

    # base game information
    base_game_version = api_responce["data"]["game"]["latest"]["version"]
    base_game_url = api_responce["data"]["game"]["latest"]["path"]
    voicepack_game_list = api_responce["data"]["game"]["latest"]["voice_packs"]
    
    download_list = []
    has_upgrade = False
    game_basefilename = None

    print("Checking current base game installation status... (This may take some time)")


    # check if game directory exist
    if not os.path.exists(PATH_DATA_GAME_GENSHIN_DIR):
        os.makedirs(PATH_DATA_GAME_GENSHIN_DIR)

    # check if it can just be upgraded instead redownloading the full game
    if(CONFIG["installed_genshin_ver"] != "0.0.0"):
        for diff in api_responce["data"]["game"]["diffs"]:
            if(diff["version"] == CONFIG["installed_genshin_ver"]):
                filename = os.path.basename(segment["path"])
                game_basefilename = os.path.splitext(filename)[0]

                download_obj = {}

                download_obj["url"] = diff["path"]
                download_obj["md5"] = diff["md5"]

                download_list.append(download_obj)
                voicepack_game_list = diff["voice_packs"]

                has_upgrade = True

    # when no upgrade avalable
    if not has_upgrade:
        for segment in api_responce["data"]["game"]["latest"]["segments"]:

            filename = os.path.basename(segment["path"])
            game_basefilename = os.path.splitext(filename)[0]
            location = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, filename)

            if not (os.path.exists(location)): #or (hashlib.md5(open(location,'rb').read()).hexdigest() != segment["md5"])
                download_obj = {}
                download_obj["url"] = segment["path"]
                download_obj["md5"] = segment["md5"]

                download_list.append(download_obj)


    print("Checking current voice pack installation status... (This may take some time)")

    # queue voicepacks
    for voice in voicepack_game_list:

        filename = os.path.basename(voice["path"])
        location = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, filename)

        if(voice["language"] in CONFIG["lang"]) and not os.path.exists(location):  #and (not (os.path.exists(location)) or (hashlib.md5(open(location,'rb').read()).hexdigest() != voice["md5"]))
            download_obj = {}

            download_obj["url"] = voice["path"]
            download_obj["md5"] = voice["md5"]

            download_list.append(download_obj)


    # Download all files
    for download in download_list:
        
        filename = os.path.basename(download["url"])
        location = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, filename)
        download_file(download["url"], location)
        print("downloading: ", filename)
        

    # if there is files in parts, combine them into 1 big file
    print("Combining zip to make it readable...")
    location = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, game_basefilename)
    parts = getZipParts(location)

    if len(parts) > 0:
        with open(location, "ab") as outfile:
            for part_filename in parts:
                part_location = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, part_filename)
                with open(part_location, "rb") as infile:
                    while True:
                        chunk = infile.read(8192)
                        if not chunk:
                            break
                        outfile.write(chunk)
                os.remove(part_location)
    print("Extract game...")
    with zipfile.ZipFile(location, 'r') as zip_ref:
        zip_ref.extractall(PATH_DATA_GAME_GENSHIN_DIR)

    CONFIG["installed_genshin_ver"] = base_game_version

    print(game_basefilename)
    print(getZipParts(location))




def getZipParts(zip_file):
    files = []
    
    game_basefilename = os.path.basename(zip_file)

    for num in range(1,999):
        part_file =  f"{game_basefilename}.{str(num).zfill(3)}"
        path = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, part_file)

        if os.path.exists(path):
            files.append(part_file)
        else:
            break

    return files
