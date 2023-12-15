#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(username, token))

    try:
        json_response = response.json()
        print(json_response.get('id'))
    except ValueError:
        print("Not a valid JSON")
