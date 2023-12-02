#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as req

if __name__ == "__main__":
    with req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print("\t- type: ", end="")
    print(type(html))
    print("\t- content: ", end="")
    print(html)
    print("\t- utf8 content: ", end="")
    print(html.decode("utf-8"))
