#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found"""
import sys
import urllib.request as req


if __name__ == "__main__":
    with req.urlopen(sys.argv[1]) as response:
        res_id = response.headers.get('X-Request-Id')
    print(res_id)
