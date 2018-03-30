# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 22:26:08 2018

@author: palash
"""
from twarc import Twarc
import csv
from urlextract import URLExtract
from textblob import TextBlob

# log in via codes provided by Twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

# create a public var to store a list of tweets
# .search method will retrieve a bunch of tweets with the designated word.
public_tweets = t.search('Apple',lang='en')

# to export to .csv
# 'with open' helps close your file automatically
with open('twitter_sentiment_analysis.csv', 'w', newline = '',encoding='utf-8') as output:
    fileOut = csv.writer(output)
    data = [['Date', 'Tweets', 'Polarity', 'Subjectivity', 'URL','Location','followers','friends','fav',]]
    
    fileOut.writerows(data)

    for tweet in public_tweets:
        date=tweet["created_at"]
        text=tweet["full_text"]
        loc = tweet["user"]["location"]
          #descrip = tweet["user"]["description"]
        followers = tweet["user"]["followers_count"]
          #print(followers)
        friends = tweet["user"]["friends_count"]
          #print(friends)
        fav = tweet["favorite_count"]
          #print(fav)
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        
        # default value for url
        # if url = None, perform operations on tweet.text to cut off existing url
        url = None

        # to start a separate column for URL
        # split texts into chunks
        words = text.split()

        # to extract link...
        link = URLExtract()

        # find links within a tweet
        urls = link.find_urls(text)

        # identify link - http / https (http is common denominator for both)
        for word in words:
            #print (word)
            if 'http' in word:
                url = word

        fileOut.writerow([date,text, polarity, subjectivity, url,loc,followers,friends,fav])
        
        # check your CSV file for clean results
