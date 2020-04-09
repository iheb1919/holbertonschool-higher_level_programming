#!/bin/bash
# 0. cURL body size
curl -sI GET "$1" | awk '/Content-Length/{print $2}'
