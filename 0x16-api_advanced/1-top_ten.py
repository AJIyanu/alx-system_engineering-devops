#!/usr/bin/python3
"""
a function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
try:
    import requests
except ImportError:
    import collections.abc
    collections.Mapping = collections.abc.Mapping
    collections.MutableMapping = collections.abc.MutableMapping
    collections.Iterable = collections.abc.Iterable
    collections.MutableSet = collections.abc.MutableSet
    collections.Callable = collections.abc.Callable
    import requests


def top_ten(subreddit):
    """prints the first 10 hot posts"""
    headers = {"User-Agent": "AJ Iyanu"}
    url = f"http://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    title = response.json()
    if title.get("data").get("dist") == 0:
        print("None")
        return
    for data in title["data"]["children"]:
        print(data["data"]["title"])
