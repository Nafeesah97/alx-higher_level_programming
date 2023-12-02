#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        val = sys.argv[1]
    else:i
        val = ""
    r = requests.post(url, data={"q": val})
    js = r.status_code()
    if js == 204:
        print("No result")
    else:
        try:
            res = r.json()
            if len(res) > 0:
                print("[{}] {}".format(res[0]["id"], res[0]["name"]))
            else:
                print("No result")
        except Exception as e:
            print("Not a valid JSON")
