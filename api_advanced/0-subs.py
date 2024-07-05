#!/usr/bin/python3
"""
A script that uses the Reddit API to output the
number of subscribers of a certain subreddit.
"""

import json
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises exception for bad responses (4xx or 5xx)

        data = response.json()
        return data['data']['subscribers']

    except requests.RequestException as e:
        print(f"Error fetching subreddit data: {e}")
        return 0
