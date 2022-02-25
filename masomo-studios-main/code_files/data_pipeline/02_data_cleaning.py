#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# remove all emojis? create a place holder?
# delete sentences with more than 30% unknown words? -> threshold?

import csv
import html


def clean_data():
    """
    :return: a csv-file with the tweets cleaned from \n, containing tweet, id, username (unique), screen name,
    number of faves, number of retweets and date-time in that order
    """
    clean = list()
    with open('../data_files/tweets.csv', newline='') as csv_f:
        reader = csv.reader(csv_f, delimiter=',')
        for row in reader:
            # format of input: date, tweet, faves, retweets, id, location, screen name, username
            date_time = row[0]
            tweet = row[1]
            faves = row[2]
            retweets = row[3]
            tweet_id = row[4]
            screen_name = row[6]
            user = row[7]
            # rough tokens:
            tweet = html.unescape(tweet)
            # remove \n
            tweet = tweet.replace('\n', ' ')
            # TODO remove further stuff...?
            # removes tweets with less than 4 words
            if len(tweet.split()) >= 4:
                clean.append([tweet_id, tweet, user, screen_name, faves, retweets, date_time])
    return clean


with open('../data_files/tweets_cleaned.csv', 'w+') as csv_write:

    header = ['id', 'tweet', 'unique_user', 'screen_name',
              'favorites', 'retweets', 'date_time']
    csvwriter = csv.writer(csv_write)
    csvwriter.writerow(header)
    for tup in clean_data():
        csvwriter.writerow(tup)
