#!/usr/bin/python3
"""
This script is a recursive function that queries the Reddit API, 
parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests
from collections import defaultdict


def count_words(subreddit, word_list, after=None, word_count=defaultdict(int)):
    """Recursive function to count words in hot post titles"""

    url = f'https://api.reddit.com/r/{subreddit}/hot'
    headers = {'User-Agent': 'my-app'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url=url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower().split()
        for word in title:
            for keyword in word_list:
                if word == keyword.lower():
                    word_count[keyword.lower()] += 1

    after = data['data']['after']
    if after is None:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print("{}: {}".format(word, count))
    else:
        count_words(subreddit, word_list, after, word_count)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
