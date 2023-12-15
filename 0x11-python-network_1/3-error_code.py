#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    # Store url
    url = sys.argv[1]

    request = urllib.request.Request(url)

    # Try to send and decode response
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read()).decode('utf-8')

    # Catch error
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
