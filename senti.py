#!usr/bin/python3
from textblob import TextBlob
import csv
import re

with open ('tweetsentiments.csv', 'a') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['twitter_tweet','sentiment','sentiment_score'])
outfile.close()

def senwrite(tweet,sentiment,score):
	with open ('tweetsentiments.csv', 'a') as outfile:
		writer = csv.writer(outfile)
		writer.writerow([tweet,sentiment,score])
	outfile.close()

with open('tweets.csv', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		ro = row[3]
		ro1 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",ro).split())
# For cleaning: (the expression above)https://stackoverflow.com/questions/8376691/how-to-remove-hashtag-user-link-of-a-tweet-using-regular-expression
# using TextBlob library for analysis
		analysetweet = TextBlob(ro1)
		if analysetweet.sentiment.polarity > 0:
			senwrite(ro1,'positive',analysetweet.sentiment.polarity)
		elif analysetweet.sentiment.polarity == 0:
			senwrite(ro1,'neutral',analysetweet.sentiment.polarity)
		else:
			senwrite(ro1,'negative',analysetweet.sentiment.polarity)
f.close()
