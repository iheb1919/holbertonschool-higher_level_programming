#!/usr/bin/python3
"""  POST an email #1"""
import sys
import requests


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    reqt = requests.post(sys.argv[1], data=values)
    print(reqt.text)
