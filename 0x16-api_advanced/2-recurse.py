#!/usr/bin/python3
import requests

"""
Using reddit's API
"""


def recurse(subreddit, hot_list=[], after=None):
    """
    Query the Reddit API and return a list containing the titles of all hot
    articles for a given subreddit. If no results are found for the given
    subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:com.example.myredditapp:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                hot_list.append(post.get('data', {}).get('title', None))
            after = data.get('data', {}).get('after', None)
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
