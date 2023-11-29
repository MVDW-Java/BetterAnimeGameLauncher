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
PATH_DATA_WINE_DIR = os.path.join(PATH_DATA_DIR, "wine")
PATH_DATA_DXVK_DIR = os.path.join(PATH_DATA_DIR, "dxvk")
PATH_DATA_GAME_DIR = os.path.join(PATH_DATA_DIR, "game")
PATH_DATA_PREFIX_DIR = os.path.join(PATH_DATA_DIR, "prefix")
PATH_MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

PLATFORM_NAME = platform.system()