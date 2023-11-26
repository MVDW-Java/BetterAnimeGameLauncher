from BetterAnimeGameLauncher import *

from BetterAnimeGameLauncher.util.cache import saveCache
from BetterAnimeGameLauncher.util.config import saveConfig

import sys
import requests
import tarfile
import io


def initWine(val):
    # Check if given wine type/version exist
    if(val != None):
        checkWine(val)

    # Create cache for installed data when needed
    if "INSTALLED" not in CACHE:
        CACHE["INSTALLED"] = {};

    # Set wine version into config
    if "WINE" not in CONFIG:
        if(val == None):
            CONFIG["WINE"] = METADATA["wine"]["DEFAULT"]
        else:
            CONFIG["WINE"] = val; 
    # Check if installed wine versions is in the cache 
    if "WINE" not in CACHE["INSTALLED"]:
        CACHE["INSTALLED"]["WINE"] = []


    if CONFIG["WINE"] not in CACHE["INSTALLED"]["WINE"]:
        downloadWine(CONFIG["WINE"])

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
    if wine_url == None:
        print(f"error: the wine url does not exist")
        sys.exit(1)

    if not os.path.exists(PATH_DATA_DIR):
        os.makedirs(PATH_DATA_DIR)

    response = requests.get(wine_url, stream=True)
    file = tarfile.open(fileobj=response.raw, mode="r|xz")
    file.extractall(PATH_DATA_DIR)

