#!/usr/bin/python3
import requests
import sys

def fetch_and_display_x_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("Value of X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in the response headers.")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    urls = [
        "http://0.0.0.0:5050",
        "http://0.0.0.0:5050",
        "http://0.0.0.0:5050"
    ]

    for url in urls:
        fetch_and_display_x_request_id(url)
