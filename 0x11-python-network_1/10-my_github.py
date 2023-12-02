#!/usr/bin/python3
"""takes your GitHub credentials uses the GitHub API to display your id"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(
            'https://httpbin.org/basic-auth/user/pass',
            auth=(username, password)
            )
    print(r.headers.get('id'))
