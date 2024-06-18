#!/usr/bin/python3
""" raddit api"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    if after is None:  # Initialize the dictionary at the start
        word_count = {word.lower(): 0 for word in word_list}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return  # Invalid subreddit or request issue

    data = response.json()

    for post in data['data']['children']:
        title = post['data']['title'].lower().split()
        for word in word_count.keys():
            word_count[word] += title.count(word)

    after = data['data']['after']
    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        # Sort the word count dictionary
        sorted_word_count = sorted(word_count.items(), key=lambda
                                   x: (-x[1], x[0]))

        # Print the sorted word counts
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".
              format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
