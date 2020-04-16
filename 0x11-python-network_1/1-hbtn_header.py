#!/usr/bin/python3
""" Response header value #0 """
import urllib.request
import sys

if __name__ == "__main__":
    """req = request.Request(sys.argv[1])"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
    print(html['X-Request-Id'])
