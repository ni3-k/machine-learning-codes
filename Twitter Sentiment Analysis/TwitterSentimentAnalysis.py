import tweepy
from textblob import TextBlob
import csv

consumer_key =  'CONSUMER_KEY_HERE'
consumer_secret = 'CONSUMER_SECRET_HERE'

access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

with open('twitter_sentiment.csv', 'w') as file:
	writer = csv.writer(file)
	writer.writerow(['Index', 'Tweet', 'Author', 'Label'])

	for i, tweet in enumerate(public_tweets):
		analysis = TextBlob(tweet.text)
		author = tweet.user.screen_name

		polarity = analysis.sentiment.polarity
		row_to_add = str(i+1) + ',' + tweet.text + ',' + author + ','

		if polarity > 0:
			file.write(row_to_add + 'Positive')
			file.write('\n')
		elif polarity == 0:
			file.write(row_to_add + 'Neutral')
			file.write('\n')
		else:
			file.write(row_to_add + 'Negative')
			file.write('\n')