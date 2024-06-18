import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return

    data = response.json()

    for post in data['data']['children']:
        title = post['data']['title'].lower().split()
        for word in word_count.keys():
            word_count[word] += title.count(word)

    after = data['data']['after']
    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        count_words(sys.argv[1], [x.lower() for x in sys.argv[2].split()])

