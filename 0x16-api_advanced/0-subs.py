#!/usr/bin/python3
"""
 a function that queries the Reddit API and returns
 the number of subscribers (not active users,
 total subscribers) for a given subreddit.
 If an invalid subreddit is given, the function should return 0.
 """
try:
    import requests
except Exception:
    pass
import json


def number_of_subscribers(subreddit):
    """
    returns numbers of subscriber
    if subreddit not valid returns 0
    """
    headers = {"User-Agent": "AJ Iyanu"}
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    users = json.loads(response.text)
    if users.get("data").get('subscribers'):
        return users.get("data").get('subscribers')
    return 0
