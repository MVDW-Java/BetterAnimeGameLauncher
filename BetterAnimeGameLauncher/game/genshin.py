from BetterAnimeGameLauncher import *

import os

def launchGenshin():
    game_path = "/home/mvdw/.var/app/moe.launcher.an-anime-game-launcher/data/anime-game-launcher/Genshin\ Impact/GenshinImpact.exe"

    wine_bin = os.path.join(PATH_DATA_WINE_DIR, CONFIG["WINE"], "bin", "wine")
    #wine_exec = f"WINEPREFIX=\"{PATH_DATA_PREFIX_DIR}\" {wine_bin} {game_path}"
    wine_exec = f"WINEPREFIX=\"{PATH_DATA_PREFIX_DIR}\" WINEDLLOVERRIDES=\"d3d11,d3d10core,dxgi,d3d9=n\" {wine_bin} {game_path}" #

    #TODO: make chdir work so it can the game in its own directory(for the DumpFile from zfbrowser)
    #os.chdir()
    os.system(wine_exec)