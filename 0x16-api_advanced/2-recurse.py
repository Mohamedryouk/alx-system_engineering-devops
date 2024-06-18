#!/usr/bin/python3
"""recurse"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """recurse func"""
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after} if after else {}
    response = requests.get(base_url, params=params,
                            headers={'User-agent': 'your bot 0.1'})
    if response.status_code == 404:
        return None
    data = response.json()
    if not data['data']['children']:
        return hot_list if hot_list else None
    hot_list.extend([article['data']['title']
                    for article in data['data']['children']])
    after = data['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
