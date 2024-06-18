#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:com.example.myredditapp:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get('data', {}).get('title', None))
        else:
            print(None)
    except requests.RequestException:
        print(None)
