#!/usr/bin/python3
"""
Search API
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        q = ""
    else:
        q = sys.argv[1]

    status = requests.post('http://0.0.0.0:5000/search_user', data={"q": q})

    try:
        if status.json():
            print("[{}] {}".format(status.json().get("id"),
                                   status.json().get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
