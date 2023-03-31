#!bin/bash 
"""Fetches https://alx-intranet.hbtn.io/status."""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read()

print("- type: {}".format(type(html)))
print("- content: {}".format(html))
print("- utf8 content: {}".format(html.decode('utf-8')))

