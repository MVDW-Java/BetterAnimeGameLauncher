from bagl import *

from bagl.util.download import download_file

import os
import zipfile

def initJadeite():
    if not os.path.exists(PATH_DATA_JADEITE_DIR):
        installJadeite()

def installJadeite():
    os.makedirs(PATH_DATA_JADEITE_DIR)

    filename = os.path.basename("jadeite.zip")
    location = os.path.join(PATH_DATA_JADEITE_DIR, filename)

    download_file("https://codeberg.org/mkrsym1/jadeite/releases/download/v3.0.11/v3.0.11.zip", location) # Quick testing

    with zipfile.ZipFile(location, 'r') as zip_ref:
        zip_ref.extractall(PATH_DATA_JADEITE_DIR)
