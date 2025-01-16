#!/usr/bin/env python3

# pip install requests tqdm

import argparse
import requests
import os
from tqdm import tqdm

def download_file(url, output):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    # If no filename is provided, use the filename from the URL
    if not output:
        output = os.path.basename(url)

    # Open the file in binary write mode and start downloading in chunks
    with open(output, 'wb') as f, tqdm(
        desc=output,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(1024):
            f.write(chunk)
            bar.update(len(chunk))

    print(f"{output} has been downloaded.")

def main():
    parser = argparse.ArgumentParser(description="A simple wget-like tool with progress bar.")
    parser.add_argument("url", help="The URL to download the file from")
    parser.add_argument("-O", "--output", help="The name of the output file")
    
    args = parser.parse_args()

    download_file(args.url, args.output)

if __name__ == "__main__":
    main()
