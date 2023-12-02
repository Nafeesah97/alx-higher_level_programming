#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as req

with req.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
