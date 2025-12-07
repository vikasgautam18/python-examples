import sys
import argparse
import requests


def shorten_url(url, api_url="http://tinyurl.com/api-create.php", timeout=10, strip=True):
    """Shorten the given URL using TinyURL API.

    Args:
        url (str): The URL to shorten.
        api_url (str): The shortening service endpoint.
        timeout (int|float): Request timeout in seconds.
        strip (bool): If True, strip whitespace from the response text.

    Returns:
        str: Shortened URL returned by the service (possibly stripped).

    Raises:
        Exception: When the service responds with a non-200 status code or
                   when the request raises an exception.
    """
    params = {'url': url}
    response = requests.get(api_url, params=params, timeout=timeout)
    if response.status_code == 200:
        text = response.text
        return text.strip() if (strip and text is not None) else text
    else:
        raise Exception(f"Error shortening URL (status {response.status_code})")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Shorten a URL using TinyURL.")
    parser.add_argument("url", help="The URL to shorten.")
    parser.add_argument("--no-strip", dest="strip", action="store_false",
                        help="Do not strip whitespace from the service response.")
    args = parser.parse_args(argv)

    try:
        short_url = shorten_url(args.url, strip=args.strip)
        print(short_url)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()