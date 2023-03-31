#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    i = response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(i.text)))
    print("\t- content: {}".format(i.text))
