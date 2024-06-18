#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:com.example.myredditapp:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
