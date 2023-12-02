#!/usr/bin/python3
"""POST request to the passed URL with the email"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email_ad = sys.argv[2]
    r = requests.post(url, data={'email': email_ad})
    re = r.text
    print('Your email is: {}'.format(re))
