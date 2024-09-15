# Bulk File Downloader

This script allows you to download multiple files from URLs listed in a `.txt` file. It utilizes multithreading to perform downloads concurrently, enhancing performance. The script also includes functionality for retrying failed downloads and logging errors.

## Features

- **Multithreaded Downloads**: Accelerates the download process by downloading multiple files simultaneously.
- **Randomized User-Agent Headers**: Helps avoid being blocked by websites by using a variety of user-agent headers.
- **Retry Mechanism**: Automatically retries failed downloads up to 3 times.
- **Progress Bar**: Displays download progress using `tqdm`.
- **Error Logging**: Logs failed download attempts and errors to separate files.

## Prerequisites

Ensure you have the following Python packages installed:

- `requests` for handling HTTP requests.
- `tqdm` for displaying a progress bar.

You can install these packages using pip:

```bash
pip install requests tqdm
```

## Usage
Prepare the URL List: Create a .txt file (e.g., 1.txt) containing the URLs of the files you want to download. Each URL should be on a new line.

Run the Script: Run the script using Python:

```bash
python download.py
```
The script will read the URLs from the .txt file, download the files, and save them to the specified output directory.

## Example
Create a file named 1.txt with the following content:

```bash
https://example.com/file1.zip
https://example.com/file2.zip
```

Run the script:

```bash
python bulk_file_downloader.py
```
The downloaded files will be saved to the downloads folder.

## Parameters
- **txt_file:** The name of the .txt file containing the list of URLs.
- **output_dir:** The directory where the downloaded files will be saved.


## Log Files
- **failed.txt:** Contains URLs that failed to download after all retry attempts.
- **errors.txt:** Contains errors that occurred during the download process, including the corresponding URLs.

## Customization
- **Retries:** You can adjust the number of retry attempts for failed downloads by modifying the retries argument in the download_file function.
- **Headers: The headers_list can be customized to add or remove user-agent headers.

## Notes
Ensure that the URLs in the .txt file are valid and accessible.
The script automatically creates the output directory if it doesn't exist.

## License
This project is free to use under the MIT License.