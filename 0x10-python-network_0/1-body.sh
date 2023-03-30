#!/bin/bash
# send a GET request to an URL with curl, and display the body of the response
curl -s -w "%{http_code}" "$1" | grep 200 && curl -s "$1"
