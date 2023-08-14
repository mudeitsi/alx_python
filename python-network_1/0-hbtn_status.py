#!/usr/bin/python3
import requests

url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for key, value in data.items():
        print("\t- {}: {}".format(key, value))
else:
    print("Failed to retrieve the data. Status code:", response.status_code)

