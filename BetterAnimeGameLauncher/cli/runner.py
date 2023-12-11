from BetterAnimeGameLauncher import *

from BetterAnimeGameLauncher.util.metadata import getComponentMetadata
from BetterAnimeGameLauncher.util.cache import getCache, saveCache
from BetterAnimeGameLauncher.util.config import getConfig

from BetterAnimeGameLauncher.component.wine import initWine
from BetterAnimeGameLauncher.component.dxvk import initDXVK

from BetterAnimeGameLauncher.game.genshin import launchGenshin
from BetterAnimeGameLauncher.game.starrail import launchHSR

def runner(args):
    args_list = vars(args)

    # Get required data from server, cache and config
    getComponentMetadata()
    getCache()
    getConfig()

    # setup components
    initWine(args_list["wine"])
    initDXVK(args_list["dxvk"])
    
    
    # launch game
    match args_list["game"]:
        case "genshin":
            print("start genshin...")
            launchGenshin()
        case "starrail":
            print("start HSR...")
            launchHSR()
