#!/usr/bin/env python3
"""
This module fetches the status from 'https://alu-intranet.hbtn.io/status'
using the requests package and prints the response content with proper tabulation.
"""

import requests

def fetch_status():
    """
    Fetches the status from the specified URL and prints the response.
    """
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

if __name__ == "__main__":
    fetch_status()

