import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


dotenv_path = os.path.join(os.path.dirname(__file__), '.gitignore')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def shorten_link(token, url):
    response_field = "link"
    short_url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    long_url = {
        "long_url": url
    }

    response = requests.post(short_url, json=long_url, headers=headers)
    response.raise_for_status()
    bitlink = response.json()[response_field]

    return bitlink


def count_clicks(token, url):
    response_field = "total_clicks"
    count_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(count_url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()[response_field]

    return clicks_count


def is_bitlink(token, url):
    is_bitlink_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(is_bitlink_url, headers=headers)

    return response.ok


def main():
    bitly_api_key = os.environ["BITLY_API_KEY"]

    parser = argparse.ArgumentParser(
        description = '''Bitly shortener and clicks counter is a console utility
            that shortens links using Bitly URL shortener and counts
            clicks by Bitlink short URL.'''
    )
    parser.add_argument('url', help='Input bitlink or url')
    args = parser.parse_args()

    initial_url = args.url
    parsed_initial_url = urlparse(initial_url)
    url_to_check = f"{parsed_initial_url.netloc}{parsed_initial_url.path}"

    if is_bitlink(bitly_api_key, url_to_check):
        try:
            clicks_count = count_clicks(bitly_api_key, url_to_check)
        except requests.exceptions.HTTPError:
            print(f"Bitlink can't give data about clicks because URL {url_to_check} is broken!")
            return
        print("Your URL clicks count: {clicks_count} time(s)")
    else:
        try:
            bitlink = shorten_link(bitly_api_key, initial_url)
        except requests.exceptions.HTTPError:
            print(f"Bitlink can't give short URL because URL {initial_url} is broken!")
            return
        print("Bitlink", bitlink)


if __name__ == "__main__":
    main()
