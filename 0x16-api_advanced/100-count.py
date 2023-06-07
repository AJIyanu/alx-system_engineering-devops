#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript,
but java should not).
"""
import re
import requests


def search_word(sentence, word):
    """returns the numbers of time a word ocur"""
    pattern = r'\b{}\b'.format(re.escape(word.lower()))
    match = re.findall(pattern, sentence.lower(), flags=re.IGNORECASE)
    return len(match)


def count_words(subreddit, wordlist, word_count={}):
    """returns a sorted list of a """
    if len(word_count) == 0:
        word_count = {word: 0 for word in wordlist}
    headers = {"User-Agent": "AJ Iyanu"}
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    if "p2a4ra8m3s" not in word_count:
        response = requests.get(url, headers=headers)
    else:
        params = {"after": word_count.get("p2a4ra8m3s")}
        response = requests.get(url, headers=headers, params=params)
    titles = response.json()
    if titles.get("data").get("dist") == 0:
        return
    print(word_count)
    for title in titles['data']['children']:
        for word in word_count:
            if word == "p2a4ra8m3s":
                continue
            word_count[word] += search_word(title['data']['title'], word)
    word_count.update({"p2a4ra8m3s": titles["data"]["after"]})
    if titles['data']['after'] is None:
        del word_count["p2a4ra8m3s"]
        alpha = sorted(word_count.items())
        count = dict(sorted(alpha, key=lambda x:x[1], reverse=True))
        print(count)
        return
    print(word_count)
    count_words(subreddit, wordlist, word_count)
