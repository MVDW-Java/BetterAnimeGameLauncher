import requests
import time
from tqdm import tqdm
import threading
from pynput import keyboard

def toggle_pause(state):
    state['paused'] = not state['paused']
    print("Download Paused" if state['paused'] else "Download Resumed")

def on_press(state, key):
    try:
        if key.char == 'p':
            toggle_pause(state)
    except AttributeError:
        pass  # Key was not a char (e.g., it might be a special key)

def download_file(url, destination, speed_limit=None):
    total_size = 0 
    downloaded_size = 0
    start_time = time.time()
    state = {'paused': False}

    # Start a thread to handle keyboard input
    keyboard_thread = threading.Thread(target=keyboard_listener, args=(state,), daemon=True)
    keyboard_thread.start()

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))

        with open(destination, 'ab') as file, tqdm(
                desc=f"Downloading {url}",
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:

            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    while state['paused']:
                        time.sleep(0.1)

                    file.write(chunk)
                    downloaded_size += len(chunk)
                    bar.update(len(chunk))

                    if speed_limit:
                        elapsed_time = time.time() - start_time
                        expected_download_time = downloaded_size / speed_limit
                        remaining_time = max(0, expected_download_time - elapsed_time)
                        time.sleep(max(0.1, remaining_time))  # Sleep at least 0.1 seconds

    print(f"Download completed: {downloaded_size} bytes downloaded.")

def keyboard_listener(state):
    with keyboard.Listener(on_press=lambda key: on_press(state, key)) as listener:
        listener.join()
