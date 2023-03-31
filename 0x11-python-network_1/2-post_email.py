#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Displays the body of the response.
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = {"email":sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
