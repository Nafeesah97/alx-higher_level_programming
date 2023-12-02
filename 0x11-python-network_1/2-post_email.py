#!/usr/bin/python3
"""POST request to the passed URL with the email as a parameter"""
import sys
import urllib.request as req
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    pos = req.Request(url, data)
    with req.urlopen(pos) as response:
        html = response.read()
        res = html.decode('utf-8')
    print(res)
