#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import emoji
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
profanities = ['4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses', 'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'ballbag', 'balls', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bloody', 'blow', 'job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum', 'bunny', 'fucker', 'butt', 'butthole', 'buttmunch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet', 'muncher', 'cawk', 'chink', 'cipa', 'cl1t', 'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot', 'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'damn', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'f', 'u', 'c', 'k', 'f', 'u', 'c', 'k', 'e', 'r', 'f4nny', 'fag', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 'fuckers', 'fuckhead', 'fuckheads', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucks', 'fuckwhit', 'fuckwit', 'fudge', 'packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux', 'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged', 'gangbangs', 'gaylord', 'gaysex', 'goatse', 'God', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex', 'hell', 'heshe', 'hoar', 'hoare', 'hoer', 'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off', 'jackoff', 'jap', 'jerk-off', 'jism', 'jiz', 'jizm', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother', 'fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'nob', 'nob', 'jokey', 'nobhead', 'nobjocky', 'nobjokey', 'numbnuts', 'nutsack', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'p0rn', 'pawn', 'pecker', 'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', 'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys', 'rectum', 'retard', 'rimjaw', 'rimming', 's', 'hit', 's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter', 'shitters', 'shitting', 'shittings', 'shitty', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated', 'xxx']


# nlp = spacy.load("en_core_web_lg")
# nlp.add_pipe('spacytextblob')

faces = [em for name, em in emoji.EMOJI_UNICODE_ENGLISH.items() if 'face' in name]

# sentiment analysis
# def get_tweets_sentiment(filename):
#     sents_tweet = list()
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             doc = nlp(row[1])
#             p = doc._.polarity
#             if p >= 0.7:
#                 sents_tweet.append((row[0], row[1], row[2], p))
#     return sents_tweet
#
# def write_sentiment_file():
#     sent_tweets = set(get_tweets_sentiment('tweets_clean.csv'))
#     with open('tweets_sentiment.csv', 'w+') as file:
#         writer = csv.writer(file)
#         for tup in sent_tweets:
#             writer.writerow(tup)

# filtering for emojis
def get_tweets_emojis(filename):
    faces_tweets = list()
    i = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for face in faces:
                if face in row[1]:
                    faces_tweets.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    return set(faces_tweets)

def write_emoji_file(infile: str, outfile: str) -> None:
    faces_tweets = set(get_tweets_emojis(infile))
    with open(outfile, 'w+') as file:
        writer = csv.writer(file)
        for tup in faces_tweets:
            writer.writerow(tup)

# filtering for nouns
def remove_non_noun(infile: str, outfile: str) -> None:
    """
    writes a csv-file at outfile with the tagged tweets cleaned from lines without NOUN tag, containing tweet, id,
    username (unique), screen name, number of faves, number of retweets, date-time and tagged tweet in that order
    """
    clean = list()
    with open(infile, newline='') as csv_f, open(outfile, 'w+') as csv_write:
        reader = csv.reader(csv_f, delimiter=',')
        writer = csv.writer(csv_write)
        for row in reader:
            # format of input: id,tweet,unique_user name,screen_name,favorites,retweets,date_time,tagged_tweets
            if 'NOUN' in row[7]:
                writer.writerow(row)
            else:
                continue


# Todo: insert profanity filter here
def remove_profanity(infile: str, outfile: str, profanities: list) -> None:
    """
    filters out each line in infile (csv) which contains any of the profanities in profanity list
    and writes it to outfile (csv)
    """
    with open(infile, newline='') as csv_f, open(outfile, 'w+') as csv_write:
        reader = csv.reader(csv_f, delimiter=',')
        writer = csv.writer(csv_write)
        for row in reader:
            contains_prof = False
            for p in profanities:
                # Only count real profane words not fragments
                if len(p) > 2:
                    if p in row[1].lower():
                        contains_prof = True
                        break
            if not contains_prof:
                writer.writerow(row)


# making sure there are no double entries
def delete_duplicates(infile, outfile):
    data = pd.read_csv(infile, names=['id', 'tweet', 'unique_user', 'screen_name',
                                                                     'favorites', 'retweets', 'date_time',
                                                                     'tagged_tweets'])

    data.drop_duplicates(subset='id', keep='first', inplace=True)
    data.to_csv(outfile, index=False)
    return None

# choose depending on which database you are trying to create
# no profanities
# remove_profanity('../data_files/tweets_filtered_emoji.csv', '../data_files/tweets_filtered_profanity2.csv', profanities)
delete_duplicates('../data_files/tweets_merged.csv', '../data_files/tweets_no_dup.csv')

# emojis
# write_emoji_file('../data_files/tweets_merged.csv', '../data_files/tweets_filtered_emoji.csv')
# delete_duplicates('../data_files/tweets_filtered_emoji.csv', '../data_files/tweets_filtered_emoji.csv')
