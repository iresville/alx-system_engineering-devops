#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request."""

if __name__ == '__main__':
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"

    # Check if an argument is given, otherwise set q to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={'q': q})

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
