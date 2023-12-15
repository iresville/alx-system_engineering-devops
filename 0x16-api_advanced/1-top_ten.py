#!/usr/bin/python3
"""
This script queries the Reddit API 
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """request title and handle errors"""
    if not subreddit:
        return None

    url = f'https://api.reddit.com/r/{subreddit}/hot'
    headers = {'User-Agent': 'my-app'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
