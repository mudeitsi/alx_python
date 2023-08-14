#!/usr/bin/env python3
"""
This module takes a URL and an email address as command-line arguments,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})
    print(response.text)

