#!/bin/bash
# displays all HTTP methods the server will accept
curl -s "$1" | grep "Allow" | cut -d' ' -f2
