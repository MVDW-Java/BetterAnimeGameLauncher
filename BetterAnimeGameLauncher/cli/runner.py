from BetterAnimeGameLauncher import *

from BetterAnimeGameLauncher.util.metadata import getComponentMetadata
from BetterAnimeGameLauncher.util.cache import getCache, saveCache
from BetterAnimeGameLauncher.util.config import getConfig

from BetterAnimeGameLauncher.component.wine import initWine
from BetterAnimeGameLauncher.component.dxvk import initDXVK


def runner(args):
    # Get required data from server, cache and config
    getComponentMetadata()
    getCache()
    getConfig()

    for att, val in vars(args).items():
        match att:
            case "wine":
                initWine(val);
            case "dxvk":
                initDXVK(val);
            
