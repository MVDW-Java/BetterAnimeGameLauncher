from bagl import *
import subprocess
import vodka
import os


script_dir = os.path.abspath(__file__)

while True:
    if os.path.basename(script_dir) == "BetterAnimeGameLauncher":
        project_root = script_dir
        break
    parent = os.path.dirname(script_dir)
    if parent == script_dir:
        raise FileNotFoundError("BetterAnimeGameLauncher directory not found.")
    script_dir = parent

SOPHON_DOWNLOADER_PATH = os.path.join(project_root, "Sophon-Downloader", "Sophon.Downloader.exe")

def SophonGameDownloader(game_id, version, output_dir):
    """
    Launch the Sophon Downloader with the specified parameters.
    
    :param game_id: The ID of the game to download.
    :param version: The version of the game to download.
    :param output_dir: The directory where the game will be downloaded.
    """
    cmd = [
        SOPHON_DOWNLOADER_PATH,
        "full",
        game_id,
        "game",
        version,
        output_dir
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Starting Sophon Downloader...")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Sophon Downloader failed with error:")
        print(e.stderr)

def SophonGameUpdater(game_id, update_from, update_to, output_dir):
    """
    Launch the Sophon Downloader to update the game.
    
    :param game_id: The ID of the game to update.
    :param update_from: The version to update from (previous version).
    :param update_to: The version to update to (new version).
    :param output_dir: The directory where the game is located.
    """
    cmd = [
        SOPHON_DOWNLOADER_PATH,
        "update",
        game_id,
        "game",
        update_from,
        update_to,
        output_dir
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Updating Sophon Updater...")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Sophon Updater update failed with error:")
        print(e.stderr)

def SophonAudioDownloader(game_id, package, version, output_dir):
    """
    Launch the Sophon Downloader to download voice packs.
    
    :param game_id: The ID of the game for which to download voice packs.
    :param package: The voice pack to download (e.g., "zh-cn", "en-us", "ja-jp", "ko-kr").
    :param version: The version of the game.
    :param output_dir: The directory where the voice pack will be downloaded.
    """
    cmd = [
        SOPHON_DOWNLOADER_PATH,
        "full",
        game_id,
        package,
        version,
        output_dir
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Downloading voice pack...")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Sophon Downloader voice pack download failed with error:")
        print(e.stderr)
        
def SophonAudioUpdater(game_id, package, update_from, update_to, output_dir):
    """
    Launch the Sophon Downloader to update voice packs.
    
    :param game_id: The ID of the game for which to update voice packs.
    :param package: The voice pack to update (e.g., "zh-cn", "en-us", "ja-jp", "ko-kr").
    :param update_from: The version to update from (previous version).
    :param update_to: The version to update to (new version).
    :param output_dir: The directory where the voice pack is located.
    """
    cmd = [
        SOPHON_DOWNLOADER_PATH,
        "update",
        game_id,
        package,
        update_from,
        update_to,
        output_dir
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Updating voice pack...")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Sophon Updater voice pack update failed with error:")
        print(e.stderr)