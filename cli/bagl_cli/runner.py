from bagl import *

from bagl.util.metadata import getComponentMetadata
from bagl.util.cache import getCache, saveCache
from bagl.util.config import getConfig

from bagl.component.wine import initWine
from bagl.component.dxvk import initDXVK

from bagl.game.genshin import launchGenshin
from bagl.game.starrail import launchHSR
from bagl.game.test import launchTest

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
        case "test":
            launchTest()
