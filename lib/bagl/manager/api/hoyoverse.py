from bagl import *

import os
import base64
import requests
import json

#Install a Hoyoverse Game
#   game_id:
#       - 0 > Honkai Impact 3rd
#       - 1 > Genshin Impact
#       - 2 > Honkai Star Rail
#       - 3 > Zenless Zone Zero
class Hoyoverse:
    def __init__(self, game_id):
        self.api = json.loads(requests.get(base64.b64decode(GAME_MAP[game_id]["API"])).content)
        self.game_id = game_id

    def listDownload(self):

        # game data
        game_name_config = GAME_MAP[self.game_id]["NAME"]
        game_name_short = GAME_MAP[self.game_id]["NAME_SHORT"]
        game_name_config = GAME_MAP[self.game_id]["NAME_CONFIG"]
        game_data_dir = GAME_MAP[self.game_id]["DATA_DIR"]

        # base game information
        base_game_version = self.api["data"]["game"]["latest"]["version"]
        base_game_url = self.api["data"]["game"]["latest"]["path"]
        voicepack_game_list = self.api["data"]["game"]["latest"]["voice_packs"]

        download_list = []
        has_upgrade = False
        game_basefilename = None

        # check if game directory exist
        if not os.path.exists(game_data_dir):
            os.makedirs(game_data_dir)


        # checking config/cahce data
        if game_name_config not in CACHE:
            CACHE[game_name_config] = {}
        if game_name_config not in CONFIG:
            CONFIG[game_name_config] = {}
        if "INSTALLED_VERSIONS" not in CACHE[game_name_config]:
            CACHE[game_name_config]["INSTALLED_VERSIONS"] = []
        if "INSTALLED_LANGUAGES" not in CACHE[game_name_config]:
            CACHE[game_name_config]["INSTALLED_VERSIONS"] = []
        if "version" not in CONFIG[game_name_config]:
            CONFIG[game_name_config]["version"] = base_game_version
        if "voice_packs" not in CONFIG[game_name_config]:
            CONFIG[game_name_config]["voice_packs"] = ["en-us"]

        # check if it can just be upgraded instead redownloading the full game
        if(len(CACHE[game_name_config]["INSTALLED_VERSIONS"]) > 0):
            for diff in self.api["data"]["game"]["diffs"]:
                if(diff["version"] in CACHE[game_name_config]["INSTALLED_VERSIONS"]):
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
            for segment in self.api["data"]["game"]["latest"]["segments"]:

                filename = os.path.basename(segment["path"])
                game_basefilename = os.path.splitext(filename)[0]
                location = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, filename)

                if not (os.path.exists(location)): #or (hashlib.md5(open(location,'rb').read()).hexdigest() != segment["md5"])
                    download_obj = {}
                    download_obj["url"] = segment["path"]
                    download_obj["md5"] = segment["md5"]

                    download_list.append(download_obj)

        # queue voicepacks
        for voice in voicepack_game_list:

            filename = os.path.basename(voice["path"])
            location = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, filename)

            if(voice["language"] in CONFIG[game_name_config]["voice_packs"]) and not os.path.exists(location):  #and (not (os.path.exists(location)) or (hashlib.md5(open(location,'rb').read()).hexdigest() != voice["md5"]))
                download_obj = {}

                download_obj["url"] = voice["path"]
                download_obj["md5"] = voice["md5"]

                download_list.append(download_obj)

        return download_list
