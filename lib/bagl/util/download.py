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

def SophonDownloader(action, game_id, package=None, version=None, update_from=None, update_to=None, output_dir=None):
    cmd = [SOPHON_DOWNLOADER_PATH, action, game_id]
    if package:
        cmd.append(package)
    if version:
        cmd.append(version)
    if update_from:
        cmd.append(update_from)
    if update_to:
        cmd.append(update_to)
    if output_dir:
        cmd.append(output_dir)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Starting Sophon Downloader with action: {action}...")
        print(f"Game ID: {game_id}, Package: {package}")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Sophon Downloader failed with error:")
        print(e.stderr)