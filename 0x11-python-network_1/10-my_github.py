#!/usr/bin/python3
"""My Github!  """
import sys
import requests

if __name__ == "__main__":
    try:
        reqt = requests.get('https://api.github.com/user',
                            auth=(sys.argv[1], sys.argv[2]))
        print(reqt.json()["id"])
    except KeyError:
        print('none')
