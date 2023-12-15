#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers (total subscribers)
for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers and handle errors appropriately"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if not subreddit:
        return 0
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    import sys
    if len(sys.argv[1]) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
