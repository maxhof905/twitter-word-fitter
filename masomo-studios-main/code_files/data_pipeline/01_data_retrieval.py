#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# masomo studios
""" retrieve tweets and save them in csv format"""

import csv
import tweepy

from twitter_keys import access_token, access_token_secret, consumer_key, consumer_secret


def store_tweets(api, filename, query, count, lang, items=1000):

    try:
        print('Initializing...')
        ids = set()
        csvFile = open(filename, 'a')
        csvWriter = csv.writer(csvFile)

        for tweet in tweepy.Cursor(api.search_tweets,
                                   q=query,
                                   count=count,
                                   lang=lang,
                                   tweet_mode='extended').items(items):

            ids.add(tweet.id)
            csvWriter.writerow([tweet.created_at,
                                tweet.full_text,  # get the full text instead of abbreviated preview)
                                tweet.favorite_count,
                                tweet.retweet_count,
                                tweet.id,
                                tweet.user.location,
                                tweet.user.name,
                                tweet.user.screen_name])

    except Exception as err:  # e.g reaching of request limit
        print('Error: {}'.format(err))
    finally:
        print('Completed!')
        csvFile.close()


def main():
    # connect to api with project/app kys generated in twitter developers lab
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # account specific
    auth.set_access_token(access_token, access_token_secret)  # project specific
    api = tweepy.API(auth, wait_on_rate_limit=True)

    if api.verify_credentials:
        print("Logged In Successfully")
    else:
        print("Error -- Could not log in with your credentials")

    print('API host:', api.host)

    # formulate query like in search function on twitter webpage (not compatible with newest api endpoint)
    search_term = "  lang:en min_faves:20000 -filter:links -filter:replies"
    store_tweets(api=api, filename='../data_files/tweets.csv', query=search_term, count=100, lang='en', items=10000)


if __name__ == '__main__':
    main()



