#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import random

from blank_generation import create_blank
from scoring import get_points


def run(tweet, tagged, tag='NOUN'):
    # overall_score = 0
    blank = create_blank(tag, tweet, tagged)    # todo: exclude sentences without any such tokens
    blanked = blank[0]
    solution = blank[1]
    print(blanked)
    inpt = input('Your guess:\t')
    points = get_points(inpt, solution)
    if points == 10:
        print('Wow, she\'s really good!')
        print('Your score is: 10')
    else:
        print(f'Your score is: {points}')
        print(f'The correct word would be: {solution}')
    print('-'*20)


#run('NOUN', 'Due to inflation 420 has gone up by 69', 'Due ADP IN prep 	to ADP IN pcomp 	inflation NOUN NN pobj 	420 NUM CD nummod 	has AUX VBZ aux 	gone VERB VBN ROOT 	up ADP RP prt 	by ADP IN prep 	69 NUM CD pobj 	')

with open('data_files/tweets_merged.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for line in reader:
        run(line[1], line[3], tag='NOUN')
