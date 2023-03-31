#!/usr/bin/env python3
"""
Displays the X-Request-Id header variable of  
a request to a given URL
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
