#!/bin/bash
# Send a GET request to the URL with the X-School-User-Id header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
