from BetterAnimeGameLauncher import *

import os
import base64
import requests
import json

# Lauch game
def launchGenshin():
    api = base64.b64decode("aHR0cHM6Ly9zZGstb3Mtc3RhdGljLmhveW92ZXJzZS5jb20vaGs0ZV9nbG9iYWwvbWRrL2xhdW5jaGVyL2FwaS9yZXNvdXJjZT9rZXk9Z2NTdGdhcmgmbGF1bmNoZXJfaWQ9MTA=")
    api_responce = json.loads(requests.get(api).content)

    # test options
    CONFIG["lang"] = ["en-us"]
    CONFIG["installed_genshin_ver"] = "4.0.0"

    # basic game info
    game_version = api_responce["data"]["game"]["latest"]["version"]
    game_executable = api_responce["data"]["game"]["latest"]["entry"]

    if(CONFIG["installed_genshin_ver"] != game_version):
        installGenshin(api_responce)

    #game_path = os.path.join(PATH_DATA_GAME_GENSHIN_DIR, game_executable)

    #wine_bin = os.path.join(PATH_DATA_WINE_DIR, CONFIG["WINE"], "bin", "wine")
    #wine_exec = f"WINEPREFIX=\"{PATH_DATA_PREFIX_DIR}\" WINEDLLOVERRIDES=\"d3d11,d3d10core,dxgi,d3d9=n\" {wine_bin} {game_path}" #


    #os.chdir(PATH_DATA_GAME_GENSHIN_DIR)
    #os.system(wine_exec)
    
    
# Install game
def installGenshin(api_responce):

    # Default values
    list_voicepacks = api_responce["data"]["game"]["latest"]["voice_packs"]

    game_download_list = []
    voice_download_list = []
    has_upgrade = False

    # check if there is an upgrade avalable
    if(CONFIG["installed_genshin_ver"] != None):
        for diff in api_responce["data"]["game"]["diffs"]:
            if(diff["version"] == CONFIG["installed_genshin_ver"]):
                list_voicepacks = diff["voice_packs"]
                game_download_list.append(diff["path"])
                has_upgrade = True

    # when no upgrade avalable
    if not has_upgrade:
        for segment in api_responce["data"]["game"]["latest"]["segments"]:
            game_download_list.append(segment["path"])

    # queue voicepacks
    for voice in list_voicepacks:
        if(voice["language"] in CONFIG["lang"]):
            voice_download_list.append(voice["path"])



    print("GAME DOWNLOAD: ", game_download_list)
    print("VOICE DOWNLOAD: ", voice_download_list)



    #print(game_executable)







# Local test to check if wine and dxvk is working fine
#def experimentalLaunchGenshin():
#    game_path = f"/home/mvdw/.var/app/moe.launcher.an-anime-game-launcher/data/anime-game-launcher/Genshin\ Impact/{game_executable}"

#    wine_bin = os.path.join(PATH_DATA_WINE_DIR, CONFIG["WINE"], "bin", "wine")
#    #wine_exec = f"WINEPREFIX=\"{PATH_DATA_PREFIX_DIR}\" {wine_bin} {game_path}"
#    wine_exec = f"WINEPREFIX=\"{PATH_DATA_PREFIX_DIR}\" WINEDLLOVERRIDES=\"d3d11,d3d10core,dxgi,d3d9=n\" {wine_bin} {game_path}" #

    #TODO: make chdir work so it can the game in its own directory(for the DumpFile from zfbrowser)
    #os.chdir()
#    os.system(wine_exec)