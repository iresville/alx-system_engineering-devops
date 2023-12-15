#!/usr/bin/env python3
from urllib.request import urlopen

response = urlopen('http://iits-jason.web.app/')

print(response.getheaders())
