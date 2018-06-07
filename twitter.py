import tweepy
import time
import json
import csv

#Twitter API
consumer_key = "s6kysVI2wT1nQUmi4PXGixuBU"
consumer_secret = "GQZyNgWeGhnToeWQs0mX6PDWRrT1n8cpuZUuEM9f4nTXdXnMl1"
access_key = "1000025271246970881-9MtsGlVvUWtxgFgPNXC9QwyIYpozYK"
access_secret = "fCeL39VcjZjKnyapl6TI7PBboJbVZgP5IaDwdV4KDgLNg"

#OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
#data
def	get_profile(screen_name):
	api = tweepy.API(auth)
	try:
		user_profile = api.get_user(screen_name)
	except tweepy.error.TweepError as e:
		user_profile = json.loads(e.response.text)

	return user_profile
#up = get_profile("realRaghavGupta")
up = get_profile("sandeep96kaur")
#print(up)
#topics
def	get_trends(location_id):
	api = tweepy.API(auth)
	try:
		trends = api.trends_place(location_id)
	except tweepy.error.TweepError as e:
		trends = json.loads(e.response.text)

	return trends
tr = get_trends("#Canada")
#print(tr)
#tweets
def get_tweets(query):
	api = tweepy.API(auth)
	try:
		tweets = api.search(q=query,count=100)
	except tweepy.error.TweepError as e:
		tweets = [json.loads(e.response.text)]

	return tweets
tw = get_tweets("#HanSolo")
#print(tw)
queries = ["#deadpool2", "\"Nova Scotia\"","@Windows","#JustinTrudeau"]

with open ('tweets.csv', 'w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['id','user','created_at','text'])
	for query in queries:
		t = get_tweets(query)
		for tweet in t:
			writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text])
