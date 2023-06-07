#!/usr/bin/python3
"""
a function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """prints the first 10 hot posts"""
    headers = {"User-Agent": "AJ Iyanu"}
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=True)
    title = response.json()
    if title.get("data").get("dist") == 0:
        print("None")
        return
    count = 1
    for data in title["data"]["children"]:
        print(data["data"]["title"])
