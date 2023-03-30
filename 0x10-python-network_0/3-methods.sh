#!/bin/bash
# Send an OPTIONS request to the URL and display the Allow header
curl -s -I -X OPTIONS "$1" | grep "Allow:" | tr -d '\r' | cut -c8-
