#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Make the request with the encoded data
    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
