import os
import platform

APP_NAME = "BetterAnimeGameLauncher"
APP_NAME_SHORT = "BAGL"
APP_DESC = ""

PATH_CONFIG_DIR = os.path.join(os.environ.get('APPDATA') or os.environ.get('XDG_CONFIG_HOME') or os.path.join(os.environ['HOME'], '.config'), APP_NAME)
PATH_CONFIG_FILE = os.path.join(PATH_CONFIG_DIR, "config.yaml")
CONFIG = {}
CONFIG_LOADED = False

PATH_CACHE_DIR = os.path.join(os.environ.get('APPDATA') or os.environ.get('XDG_CACHE_HOME') or os.path.join(os.environ['HOME'], '.cache'), APP_NAME)
PATH_CACHE_FILE = os.path.join(PATH_CACHE_DIR, "cache.json")
CACHE = {}
CACHE_LOADED = False

METADATA = {}

OLD_API_URL = "aHR0cHM6Ly9zZy1oeXAtYXBpLmhveW92ZXJzZS5jb20vaHlwL2h5cC1jb25uZWN0L2FwaS9nZXRHYW1lUGFja2FnZXM/Z2FtZV9pZHNbXT01VElWdnZjd3RNJmdhbWVfaWRzW109Z29wUjZDdWZyMyZnYW1lX2lkc1tdPXdrRTVQNVdzSWYmZ2FtZV9pZHNbXT11eEI0TUM3bnpDJmdhbWVfaWRzW109ZzBtTUl2c2hEYiZnYW1lX2lkc1tdPTR6aXlzcVhPUTgmZ2FtZV9pZHNbXT1VNWhiZHNUOVc3JmdhbWVfaWRzW109YnhQVFhTRVQ1dCZsYXVuY2hlcl9pZD1WWVRwWGxiV284"
SOPHON_API_URL = "aHR0cHM6Ly9zZy1oeXAtYXBpLmhveW92ZXJzZS5jb20vaHlwL2h5cC1jb25uZWN0L2FwaS9nZXRHYW1lQnJhbmNoZXM/bGF1bmNoZXJfaWQ9VllUcFhsYldvOCZnYW1lX2lkc1tdPTVUSVZ2dmN3dE0mZ2FtZV9pZHNbXT1nb3BSNkN1ZnIzJmdhbWVfaWRzW109d2tFNVA1V3NJZiZnYW1lX2lkc1tdPXV4QjRNQzduekMmZ2FtZV9pZHNbXT1nMG1NSXZzaERiJmdhbWVfaWRzW109NHppeXNxWE9ROCZnYW1lX2lkc1tdPVU1aGJkc1Q5VzcmZ2FtZV9pZHNbXT1ieFBUWFNFVDV0"

PATH_DATA_DIR = os.path.join(os.environ.get('APPDATA') or os.environ.get('XDG_DATA_HOME') or os.path.join(os.environ['HOME'], '.local', 'share'), APP_NAME)
PATH_DATA_PREFIX_DIR = os.path.join(PATH_DATA_DIR, "prefix")
PATH_DATA_WINE_DIR = os.path.join(PATH_DATA_DIR, "wine")
PATH_DATA_DXVK_DIR = os.path.join(PATH_DATA_DIR, "dxvk")
PATH_DATA_JADEITE_DIR = os.path.join(PATH_DATA_DIR, "jadeite")
PATH_DATA_GAME_DIR = os.path.join(PATH_DATA_DIR, "game")

PATH_DATA_GAME_GENSHIN_DIR = os.path.join(PATH_DATA_GAME_DIR, "genshin_impact")
PATH_DATA_GAME_HONKAI3RD_GLOBAL_DIR = os.path.join(PATH_DATA_GAME_DIR, "honkai_3rd_global")
PATH_DATA_GAME_HONKAI3RD_TAIWAN_DIR = os.path.join(PATH_DATA_GAME_DIR, "honkai_3rd_taiwan")
PATH_DATA_GAME_HONKAI3RD_KOREA_DIR = os.path.join(PATH_DATA_GAME_DIR, "honkai_3rd_korea")
PATH_DATA_GAME_HONKAI3RD_JAPAN_DIR = os.path.join(PATH_DATA_GAME_DIR, "honkai_3rd_japan")
PATH_DATA_GAME_ZZZ_DIR = os.path.join(PATH_DATA_GAME_DIR, "zenless_zone_zero")
PATH_DATA_GAME_STARRAIL_DIR = os.path.join(PATH_DATA_GAME_DIR, "honkai_starrail")
PATH_DATA_GAME_PGR_DIR = os.path.join(PATH_DATA_GAME_DIR, "punishing_gray_raven")
PATH_DATA_GAME_RE1999_DIR = os.path.join(PATH_DATA_GAME_DIR, "reverse_1999")

GAME_MAP = {
    0: {
        "NAME": "Honkai Impact 3rd Global",
        "NAME_SHORT": "HI3GLB",
        "NAME_CONFIG": "honkai_impact_3rd_global",
        "GAME_ID": "5TIVvvcwtM",
        "DATA_DIR": PATH_DATA_GAME_HONKAI3RD_GLOBAL_DIR
    },
    1: {
        "NAME": "Honkai Impact 3rd Taiwan",
        "NAME_SHORT": "HI3TWN",
        "NAME_CONFIG": "honkai_impact_3rd_taiwan",
        "GAME_ID": "wkE5P5WsIf",
        "DATA_DIR": PATH_DATA_GAME_HONKAI3RD_TAIWAN_DIR
    },
    2: {
        "NAME": "Honkai Impact 3rd Korea",
        "NAME_SHORT": "HI3KOR",
        "NAME_CONFIG": "honkai_impact_3rd_korea",
        "GAME_ID": "uxB4MC7nzC",
        "DATA_DIR": PATH_DATA_GAME_HONKAI3RD_KOREA_DIR
    },
    3: {
        "NAME": "Honkai Impact 3rd Japan",
        "NAME_SHORT": "HI3JPN",
        "NAME_CONFIG": "honkai_impact_3rd_japan",
        "GAME_ID": "g0mMIvshDb",
        "DATA_DIR": PATH_DATA_GAME_HONKAI3RD_JAPAN_DIR
    },
    4: {
        "NAME": "Genshin Impact",
        "NAME_SHORT": "GI",
        "NAME_CONFIG": "genshin_impact",
        "GAME_ID": "gopR6Cufr3",
        "DATA_DIR": PATH_DATA_GAME_GENSHIN_DIR
    },
    5: {
        "NAME": "Honkai: Star Rail",
        "NAME_SHORT": "HSR",
        "NAME_CONFIG": "honkai_starrail",
        "GAME_ID": "4ziysqXOQ8",
        "DATA_DIR": PATH_DATA_GAME_STARRAIL_DIR
    },
    6: {
        "NAME": "Zenless Zone Zero",
        "NAME_SHORT": "ZZZ",
        "NAME_CONFIG": "zenless_zone_zero",
        "GAME_ID": "U5hbdsT9W7",
        "DATA_DIR": PATH_DATA_GAME_ZZZ_DIR
    },
    # 7: {
    #     "NAME": "Punishing: Gray Raven",
    #     "NAME_SHORT": "PGR",
    #     "NAME_CONFIG": "punishing_gray_raven",
    #     "DATA_DIR": PATH_DATA_GAME_PGR_DIR,
        
    # },
    # 8: {
    #     "NAME": "Reverse: 1999",
    #     "NAME_SHORT": "RE1999",
    #     "NAME_CONFIG": "reverse_1999",
    #     "DATA_DIR": PATH_DATA_GAME_RE1999_DIR,
        
    # }
}

PATH_MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

PLATFORM_NAME = platform.system()
