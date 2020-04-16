#!/usr/bin/python3
""" POST an email #0 """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode()
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode()
    print(html)
