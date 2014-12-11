#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


api.update_status('Iniciando :D')

yo=api.home_timeline(trim_user=True)

ultimoTweet = yo[0].id
tweets = api.search(q='python',lang="es", since_id=ultimoTweet)
total=0


tweets = api.search(q='python', since_id=ultimoTweet)
for tweet in tweets:
    if not "RT" in tweet.text and not "@" in tweet.text:
        total+=1
        print tweet.id
        print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print "Retweet a:"
        print tweet.author.name
        print tweet.text
        api.retweet(tweet.id)


        if(ultimoTweet<tweet.id):
            ultimoTweet=tweet.id
        time.sleep(5)

    if(total>0):
        api.update_status('LOCOS POR PYTHON :D. '+ str(total)+' nuevos retweets')
        total=0
    print "ADMINISTRACIÓN: TOCA ESPERAR :S"
    time.sleep(60)
