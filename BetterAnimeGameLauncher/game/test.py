from BetterAnimeGameLauncher import *

from BetterAnimeGameLauncher.util.download import download_file
from BetterAnimeGameLauncher.util.cache import saveCache
from BetterAnimeGameLauncher.util.config import saveConfig

from BetterAnimeGameLauncher.manager.api.hoyoverse import Hoyoverse



import os
import base64
import requests
import json
import hashlib
import zipfile


# Lauch game
def launchTest():
    game = Hoyoverse(2);
    print(game.listDownload())
