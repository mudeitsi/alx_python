#!/usr/bin/env python3
"""
This module takes GitHub username and a personal access token as command-line
arguments, and uses the GitHub API to display the user's GitHub ID.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get('https://api.github.com/user', auth=(username, token))

    try:
        print(response.json().get('id'))
    except ValueError:
        print("Not a valid JSON")

