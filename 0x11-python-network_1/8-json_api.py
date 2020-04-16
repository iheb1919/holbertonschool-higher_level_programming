#!/usr/bin/python3
""" Search API """
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''
    try:
        reqt = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        req2 = req.json()
        if not req2:
            print("No result")
            exit()
        else:
            print("[{}] {}".format(req2['id'], req2['name']))
    except ValueError:
        print("Not a valid JSON")
