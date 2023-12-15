#!/usr/bin/python3
"""
This script is a recursive function that queries the Reddit API and returns a list 
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recurse the list of hot articles"""
    if not subreddit:
        return None

    url = f'https://api.reddit.com/r/{subreddit}/hot'
    headers = {'User-Agent': 'my-app'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url=url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)


if __name__ == '__main__':
    subreddit = input("Enter the subreddit: ")
    result = recurse(subreddit)
    if result:
        for title in result:
            print(title)
    else:
        print(None)
