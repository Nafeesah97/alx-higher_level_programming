#!/usr/bin/python3
"""catches error"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            r = response.read().decode('utf-8')
            print(r)
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
