#!/usr/bin/env python3
import urllib.request as ur
import urllib.error

try:
    response = ur.urlopen('http://google.com/hetlerabs/')
    print("Request sent successfully")
except urllib.error.HTTPError as e:
    print('Status: ', e.code)
    print('Reason: ', e.reason)
    print('URL: ', e.url)
