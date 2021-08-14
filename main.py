import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


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


def parsed_args():
    parser = argparse.ArgumentParser(
        description="Bitly shortener and clicks counter is a console utility \
            that shortens links using Bitly URL shortener and counts \
            clicks by Bitlink short URL."
    )
    parser.add_argument("url", help="Input bitlink or url")
    return parser.parse_args()


def get_clicks_count(token, url):
    try:
        clicks_count = count_clicks(token, url)
    except requests.exceptions.HTTPError:
        print(
            f"Bitlink can't give data about clicks because URL \
            {url} is broken!")
        return
    return clicks_count


def get_bitlink(token, url):
    try:
        bitlink = shorten_link(token, url)
    except requests.exceptions.HTTPError:
        print(
            f"Bitlink can't give short URL because URL \
            {url} is broken!")
        return
    return bitlink


def main():
    load_dotenv()

    bitly_api_key = os.environ["BITLY_API_KEY"]

    initial_url = parsed_args().url
    parsed_initial_url = urlparse(initial_url)
    url_to_check = f"{parsed_initial_url.netloc}{parsed_initial_url.path}"

    if is_bitlink(bitly_api_key, url_to_check):
        print(
            f"Your URL clicks count: {get_clicks_count(bitly_api_key, url_to_check)} time(s)")
    else:
        print(f"Bitlink {get_bitlink(bitly_api_key, initial_url)}")


if __name__ == "__main__":
    main()
