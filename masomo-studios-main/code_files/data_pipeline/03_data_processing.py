#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tag the clean tweets column of the input file and save it in outfile.tsv
"""
# -> spacy
# tokenizing
# pos tagging

import csv
import spacy

nlp = spacy.load("en_core_web_lg")

with open('../data_files/tweets_cleaned.csv', 'r') as csv_file, \
        open('../data_files/tweets_processed.tsv', 'w+') as tsv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        # todo: add id!
        doc = nlp(row[1])   # clean tweet
        tagged = list()
        tsv_file.write(f'\n')
        for token in doc:
            tagged.append([token.text, token.pos_, token.tag_, token.dep_])
        for tok in tagged:
            for info in tok:
                tsv_file.write(info + ' ')
            tsv_file.write('\t')

print('ok done.')
