import requests
import argparse

def shorten_url(url):
    api_url = "http://tinyurl.com/api-create.php"
    params = {'url': url}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Error shortening URL")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shorten a URL using TinyURL.")
    parser.add_argument("--url", required=True, help="The URL to shorten.")
    args = parser.parse_args()

    try:
        short_url = shorten_url(args.url)
        print("Shortened URL:", short_url)
    except Exception as e:
        print(str(e))