#!/usr/bin/python3
"""
queries the Reddit API and returns a list
containing the titles of all hot articles
for a given subreddit. If no results are
found for the given subreddit, the function
should return None.
"""
import requests


def recurse(subreddit, hot_list=[0]):
    """returns all titles and None for invalid"""
    headers = {"User-Agent": "AJ Iyanu"}
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": hot_list[0]}
    if hot_list[0] != 0:
        response = requests.get(url, headers=headers, params=params)
    else:
        response = requests.get(url, headers=headers)
    title = response.json()
    if title.get("data").get("dist") == 0:
        return
    hot_list[0] = title["data"]["after"]
    count = 0
    for data in title["data"]["children"]:
        hot_list.append(data["data"]["title"])
        count += 1
    if hot_list[0] is None:
        hot_list.pop(0)
        return hot_list
    return recurse(subreddit, hot_list)
