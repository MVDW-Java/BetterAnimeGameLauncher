
import requests

def download_file(url, destination):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(destination, 'ab') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
