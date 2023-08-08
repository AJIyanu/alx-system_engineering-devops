#!/usr/bin/python3
"""
 a function that queries the Reddit API and returns
 the number of subscribers (not active users,
 total subscribers) for a given subreddit.
 If an invalid subreddit is given, the function should return 0.
 """
import requests


def number_of_subscribers(subreddit):
    """
    returns numbers of subscriber
    if subreddit not valid returns 0
    """
    headers = {"User-Agent": "AJ Iyanu"}
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code != 200:
        return 0
    users = response.json()
    if users.get("data").get('subscribers'):
        return users.get("data").get('subscribers')
    return 0
