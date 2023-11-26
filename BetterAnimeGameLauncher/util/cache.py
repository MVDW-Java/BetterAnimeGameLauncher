from BetterAnimeGameLauncher import *

import os
import json


def getCache():
    global CACHE_LOADED;

    if CACHE_LOADED:
        return

    if not os.path.exists(PATH_CACHE_DIR):
        os.makedirs(PATH_CACHE_DIR)
        
    if os.path.exists(PATH_CACHE_FILE):
        with open(PATH_CACHE_FILE, 'r') as file:
            CACHE = json.load(file)
            CACHE_LOADED = True

def saveCache():
    with open(PATH_CACHE_FILE, 'w') as file:
        json.dump(CACHE, file)

