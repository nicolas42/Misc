#!/usr/bin/env python3


# pip install requests

# chmod +x wgetpy.py

# install
# sudo mv wgetpy.py /usr/local/bin/wgetpy

import argparse
import requests
import os

def download_file(url, output):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # If no filename is provided, use the filename from the URL
        if not output:
            output = os.path.basename(url)
        with open(output, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"{output} has been downloaded.")
    else:
        print(f"Failed to download. Status code: {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description="A simple wget-like tool.")
    parser.add_argument("url", help="The URL to download the file from")
    parser.add_argument("-O", "--output", help="The name of the output file")
    
    args = parser.parse_args()

    download_file(args.url, args.output)

if __name__ == "__main__":
    main()
