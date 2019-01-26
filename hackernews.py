#1. Within server.py call the hacker news api, fetch the latest comments, and run sentiment analysis on it.

#latest comments

import requests

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
stories = response.json()

comments = []
for comment in stories:
	current_url = https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty.format(comments)
	current = requests.get(current_url)
	comments.append(current.json())

for comment in comments:
	comment = comment['text']

	