from bagl import *

from bagl.util.cache import getCache

import requests
import json

component_resources = {
    "wine": "https://www.enthix.net/BAGL/wine.json",
    "dxvk": "https://www.enthix.net/BAGL/dxvk.json",
}


def getComponentMetadata():
    getCache()
    for component_type, url in component_resources.items():
        response = requests.get(url)

        if response.status_code == 200:
            CACHE[component_type] = response.json()

        METADATA[component_type] = CACHE[component_type];
