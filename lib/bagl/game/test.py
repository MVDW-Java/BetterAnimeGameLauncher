from bagl import *

from bagl.util.download import download_file
from bagl.util.cache import saveCache
from bagl.util.config import saveConfig

from bagl.manager.api.hoyoverse import Hoyoverse



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
