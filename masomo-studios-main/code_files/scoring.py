#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# what
# nltk wordnet!! + synsets?
# check for misspelling -> levenshtein
from emoji import UNICODE_EMOJI
import spacy
import unicodedata


# how to make this
nlp = spacy.load("en_core_web_lg")


def dice_coefficient(a, b):
    # whole function from wikipedia (https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Dice%27s_coefficient)
    """dice coefficient 2nt/(na + nb)."""
    if not len(a) or not len(b):
        return 0.0
    if len(a) == 1:
        a = a + u'.'
    if len(b) == 1:
        b = b + u'.'

    a_bigram_list = []
    for i in range(len(a) - 1):
        a_bigram_list.append(a[i:i + 2])
    b_bigram_list = []
    for i in range(len(b) - 1):
        b_bigram_list.append(b[i:i + 2])

    a_bigrams = set(a_bigram_list)
    b_bigrams = set(b_bigram_list)
    overlap = len(a_bigrams & b_bigrams)
    dice_coeff = overlap * 2.0 / (len(a_bigrams) + len(b_bigrams))
    return dice_coeff


def levenshteinDistance(s1, s2):
    # whole code_files from stackoverflow (https://stackoverflow.com/questions/2460177/edit-distance-in-python)
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


def get_score(usr_input, real):
    if usr_input.lower() == real.lower():
        return 'same', 1
    if levenshteinDistance(usr_input.lower(), real.lower()) <= 3:
        leven = levenshteinDistance(usr_input.lower(), real.lower())
        if leven == 1:
            return 'leven', 0.9
        if leven == 2:
            return 'leven', 0.8
        if leven == 3:
            return 'leven', 0.7
    try:
        # code_files from stack (https://stackoverflow.com/questions/53453559/similarity-in-spacy)
        doc1 = nlp(usr_input)
        doc2 = nlp(real)
        highest = round(doc1.similarity(doc2), 1)
        score = 'sim'

        dice = dice_coefficient(usr_input.lower(), real.lower())
        if highest < dice:
            highest = dice
            score = 'dice'

        return score, highest

    except IndexError:
        return 'dice', dice


def get_points(usr_input, real):
    score = get_score(usr_input, real)[1]
    return round(score*10)


def scoring_emoji(usr_input, real):
    if usr_input == real:
        return 'yay, your guess is correct!'
    else:
        return 'nay, your guess is wrong.'




# print(get_score('woman', 'Woman'))
# print(get_score('woman', 'man'))
# print(get_score('woman', 'womsn'))

