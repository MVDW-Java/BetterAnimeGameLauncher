import os
import platform

APP_NAME = "BetterAnimeGameLauncher"
APP_NAME_SHORT = "BAGL"
APP_DESC = ""

PATH_CONFIG_DIR = os.path.join(os.environ.get('APPDATA') or os.environ.get('XDG_CONFIG_HOME') or os.path.join(os.environ['HOME'], '.config'), APP_NAME)
PATH_CONFIG_FILE = os.path.join(PATH_CONFIG_DIR, "config.yaml");
CONFIG = {}
CONFIG_LOADED = False

PATH_CACHE_DIR = os.path.join(os.environ.get('APPDATA') or os.environ.get('XDG_CACHE_HOME') or os.path.join(os.environ['HOME'], '.cache'), APP_NAME)
PATH_CACHE_FILE = os.path.join(PATH_CACHE_DIR, "cache.json");
CACHE = {}
CACHE_LOADED = False

METADATA = {}

PATH_DATA_DIR = os.path.join(os.environ.get('APPDATA') or os.environ.get('XDG_DATA_HOME') or os.path.join(os.environ['HOME'], '.local', 'share'), APP_NAME)
PATH_DATA_PREFIX_DIR = os.path.join(PATH_DATA_DIR, "prefix")
PATH_DATA_WINE_DIR = os.path.join(PATH_DATA_DIR, "wine")
PATH_DATA_DXVK_DIR = os.path.join(PATH_DATA_DIR, "dxvk")
PATH_DATA_JADEITE_DIR = os.path.join(PATH_DATA_DIR, "jadeite")
PATH_DATA_GAME_DIR = os.path.join(PATH_DATA_DIR, "game")

PATH_DATA_GAME_GENSHIN_DIR = os.path.join(PATH_DATA_GAME_DIR, "genshin_impact")
PATH_DATA_GAME_HONKAI3RD_DIR = os.path.join(PATH_DATA_GAME_DIR, "honkai_3rd")
PATH_DATA_GAME_STARRAIL_DIR = os.path.join(PATH_DATA_GAME_DIR, "honkai_starrail")
PATH_DATA_GAME_PGR_DIR = os.path.join(PATH_DATA_GAME_DIR, "punishing_gray_raven")
PATH_DATA_GAME_RE1999_DIR = os.path.join(PATH_DATA_GAME_DIR, "reverse_1999")

GAME_MAP = {
    0: {
        "NAME": "Honkai Impact 3rd",
        "NAME_SHORT": "HI3",
        "NAME_CONFIG": "honkai_impact_3rd",
        "DATA_DIR": os.path.join(PATH_DATA_GAME_DIR, "honkai_3rd")
        
    },
    1: {
        "NAME": "Genshin Impact",
        "NAME_SHORT": "GI",
        "NAME_CONFIG": "genshin_impact",
        "DATA_DIR": os.path.join(PATH_DATA_GAME_DIR, "genshin_impact"),
        "API": "aHR0cHM6Ly9zZGstb3Mtc3RhdGljLmhveW92ZXJzZS5jb20vaGs0ZV9nbG9iYWwvbWRrL2xhdW5jaGVyL2FwaS9yZXNvdXJjZT9rZXk9Z2NTdGdhcmgmbGF1bmNoZXJfaWQ9MTA="
    },
    2: {
        "NAME": "Honkai: Star Rail",
        "NAME_SHORT": "HSR",
        "NAME_CONFIG": "honkai_starrail",
        "DATA_DIR": os.path.join(PATH_DATA_GAME_DIR, "honkai_starrail"),
        "API": "aHR0cHM6Ly9oa3JwZy1sYXVuY2hlci1zdGF0aWMuaG95b3ZlcnNlLmNvbS9oa3JwZ19nbG9iYWwvbWRrL2xhdW5jaGVyL2FwaS9yZXNvdXJjZT9jaGFubmVsX2lkPTEma2V5PXZwbE9WWDhWbjdjd0c4eWImbGF1bmNoZXJfaWQ9MzU="
    },
    3: {
        "NAME": "Zenless Zone Zero",
        "NAME_SHORT": "ZZZ",
        "NAME_CONFIG": "zenless_zone_zero",
        "DATA_DIR": os.path.join(PATH_DATA_GAME_DIR, "zenless_zone_zero")
    },
    4: {
        "NAME": "Punishing: Gray Raven",
        "NAME_SHORT": "PGR",
        "NAME_CONFIG": "punishing_gray_raven",
        "DATA_DIR": os.path.join(PATH_DATA_GAME_DIR, "punishing_gray_raven")
    },
    5: {
        "NAME": "Reverse: 1999",
        "NAME_SHORT": "RE1999",
        "NAME_CONFIG": "reverse_1999",
        "DATA_DIR": os.path.join(PATH_DATA_GAME_DIR, "reverse_1999")
    }
}

PATH_MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

PLATFORM_NAME = platform.system()
