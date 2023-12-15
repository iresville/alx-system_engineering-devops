#!/usr/bin/env python3
from urllib.request import urlopen, build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar

cookie_jar = CookieJar()

opener = build_opener(HTTPCookieProcessor(cookie_jar))

response = urlopen('http://iits-jason.web.app/')

cookies = list(cookie_jar)

print(len(cookie_jar))

print(cookies)
