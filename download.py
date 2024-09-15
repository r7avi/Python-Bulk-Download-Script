import os
import requests
import threading
import random
from tqdm import tqdm

lock = threading.Lock()

headers_list = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Encoding': 'gzip, deflate, br',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept-Encoding': 'gzip, deflate, br',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
        'Accept-Encoding': 'gzip, deflate, br',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
    },
]

def download_file(url, output_dir, pbar, retries=3):
    headers = random.choice(headers_list)

    try:
        filename = url.split('/')[-1]
        filepath = os.path.join(output_dir, filename)

        if not os.path.exists(filepath):
            for _ in range(retries):
                response = requests.get(url, headers=headers, stream=True, timeout=10)
                if response.status_code == 200:
                    with open(filepath, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    with lock:
                        pbar.update(1)
                    break  # Successful download, exit loop
                else:
                    # Retry if unsuccessful
                    continue
            else:
                # If all retries failed, log the URL to failed.txt
                with open('failed.txt', 'a') as f:
                    f.write(url + '\n')
        else:
            with lock:
                pbar.update(1)
    except Exception as e:
        # Log the error along with the URL to errors.txt
        with open('errors.txt', 'a') as f:
            f.write(f"Error downloading {url}: {str(e)}\n")

def bulk_download_from_txt(txt_file, output_dir):
    with open(txt_file, 'r') as file:
        links = file.readlines()

    total_links = len(links)

    with tqdm(total=total_links, desc="Downloading Files", unit="file") as pbar:
        for url in links:
            url = url.strip()
            t = threading.Thread(target=download_file, args=(url, output_dir, pbar))
            t.start()

if __name__ == "__main__":
    txt_file = "1.txt"
    output_dir = "downloads"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    bulk_download_from_txt(txt_file, output_dir)
