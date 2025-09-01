import requests
from tqdm import tqdm

url = 'https://download-cdn.jetbrains.com/python/pycharm-2025.1.3.1.exe'

response = requests.get(url, stream=True)
total_expected_bytes = int(response.headers.get("Content-Length", 0))

progress_bar = tqdm(total=total_expected_bytes, unit='iB', unit_scale=True)

with open("py.exe", "wb") as fd:
    for chunk in response.iter_content(chunk_size=128):
        if chunk:  # filter out keep-alive chunks
            fd.write(chunk)
            progress_bar.update(len(chunk))

progress_bar.close()
