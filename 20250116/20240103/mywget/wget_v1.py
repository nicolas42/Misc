import requests

def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"{filename} has been downloaded.")
    else:
        print(f"Failed to download. Status code: {response.status_code}")

# Example usage
url = 'https://ftp.gnu.org/gnu/wget/wget-latest.tar.gz'
filename = 'wget-latest.tar.gz'
download_file(url, filename)
