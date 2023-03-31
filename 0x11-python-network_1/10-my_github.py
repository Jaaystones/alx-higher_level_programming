#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
  - Uses Basic Authentication to access the ID of a Github account.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    result = requests.get("https://api.github.com/user", auth=auth)
    print(result.json().get("id"))
