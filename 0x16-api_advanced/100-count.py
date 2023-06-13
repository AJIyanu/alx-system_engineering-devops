#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript,
but java should not).
"""
import requests


def search_word(sentence, word):
    """returns the numbers of time a word ocur"""
    sentence = sentence.lower().split()
    count = 0
    for split in sentence:
        if word is split:
            count += 1
    return count


def count_words(subreddit, wordlist, word_count={}):
    """returns a sorted list of a """
    if len(word_count) == 0:
        word_count = {word.lower(): 0 for word in wordlist}
    headers = {"User-Agent": "AJ Iyanu"}
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    if "p2a4ra8m3s" not in word_count:
        response = requests.get(url, headers=headers)
    else:
        params = {"after": word_count.get("p2a4ra8m3s")}
        response = requests.get(url, headers=headers, params=params)
    titles = response.json()
    if "error" in titles:
        print("returning", titles)
        return
    for title in titles['data']['children']:
        for word in word_count:
            if word == "p2a4ra8m3s":
                continue
            word_count[word] += search_word(title['data']['title'], word)
    word_count.update({"p2a4ra8m3s": titles["data"]["after"]})
    if titles['data']['after'] is None:
        del word_count["p2a4ra8m3s"]
        alpha = sorted(word_count.items())
        count = sorted(alpha, key=lambda x: x[1], reverse=True)
        for key, value in count:
            if value != 0:
                print("{}: {}".format(key, value))
        return
    count_words(subreddit, wordlist, word_count)
