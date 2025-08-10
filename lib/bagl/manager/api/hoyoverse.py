from bagl import *
from bagl.util.download import *


import os
import base64
import requests
import json

#? Install a Hoyoverse Game
#? game_id:
#*      0: Honkai Impact 3rd Global
#*      1: Honkai Impact 3rd Taiwan
#*      2: Honkai Impact 3rd Korea
#*      3: Honkai Impact 3rd Japan
#*      4: Genshin Impact
#*      5: Honkai: Star Rail
#*      6: Zenless Zone Zero
#!      7: Punishing Gray Raven
#!      8: Reverse 1999

#TODO
# add language choice

class Hoyoverse:
    def __init__(self, game_id):
        if game_id in [4, 5, 6]: self.api_url = SOPHON_API_URL 
        else: self.api_url = OLD_API_URL
        
        self.api = json.loads(requests.get(base64.b64decode(self.api_url)).content)
        self.game_id = game_id
        self.has_upgrade = False

    def listDownload(self):

        # game data
        game_name_config = GAME_MAP[self.game_id]["NAME"]
        game_name_short = GAME_MAP[self.game_id]["NAME_SHORT"]
        game_name_config = GAME_MAP[self.game_id]["NAME_CONFIG"]
        game_data_dir = GAME_MAP[self.game_id]["DATA_DIR"]
        game_id = GAME_MAP[self.game_id]["GAME_ID"]
        
        # api branches
        branches = self.api["data"]["game_branches"] if self.api_url == SOPHON_API_URL else self.api["data"]["game_packages"]

        # base game information
        if self.api_url == SOPHON_API_URL:
            for branch in branches:
                if branch["game"]["id"] == game_id:
                    base_game_version = branch["main"]["tag"]
                    break
                
        if self.api_url == OLD_API_URL:
            for branch in branches:
                if branch["game"]["id"] == game_id:
                    base_game_version = branch["main"]["major"]["version"]
                    break



        # check if game directory exist
        if not os.path.exists(game_data_dir):
            os.makedirs(game_data_dir)


        # checking config/cache data
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
        new_version = None

        if(len(CACHE[game_name_config]["INSTALLED_VERSIONS"]) > 0):
            for branch in branches:
                if branch["game"]["id"] == game_id:
                    if self.api_url == SOPHON_API_URL and branch["main"]["tag"] != CONFIG[game_name_config]["version"]:
                        new_version = branch["main"]["tag"]
                        self.has_upgrade = True
                        break
                    elif self.api_url == OLD_API_URL and branch["main"]["major"]["version"] != CONFIG[game_name_config]["version"]:
                        new_version = branch["main"]["major"]["version"]
                        self.has_upgrade = True
                        break

        # when no upgrade avalable
        if not self.has_upgrade:
            print(f"Downloading {game_name_short} {base_game_version}...")
            SophonGameDownloader(
                game_id=game_id,
                version=base_game_version,
                output_dir=game_data_dir
            )
            print(f"{game_name_short} {base_game_version} downloaded successfully!")

            print("Downloading voice packs...")
            for voice_pack in CONFIG[game_name_config]["voice_packs"]:
                SophonAudioDownloader(
                    game_id=game_id,
                    package=voice_pack,
                    version=base_game_version,
                    output_dir=game_data_dir
                )
            print("Voice packs downloaded successfully!")

            #? update config/cache
            
        # when upgrade is available
        if self.has_upgrade:
            print(f"Updating {game_name_short} to {new_version}...")
            SophonGameUpdater(
                game_id=game_id,
                update_from=CONFIG[game_name_config]["version"],
                update_to=new_version,
                output_dir=game_data_dir
            )
            print(f"{game_name_short} updated to {new_version} successfully!")

            # sophon update voice packs
            print("Updating voice packs...")
            for voice_pack in CONFIG[game_name_config]["voice_packs"]:
                SophonAudioUpdater(
                    game_id=game_id,
                    package=voice_pack,
                    version=new_version,
                    output_dir=game_data_dir
                )
            print("Voice packs updated successfully!")
            
            #? update config/cache