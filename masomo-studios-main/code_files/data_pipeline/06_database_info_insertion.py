#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2, csv, regex

DB_NAME = "team_f_db"
DB_USER = "postgres"
DB_PASS = "d3e8db4016b1e148da8a12e4f361be44"
DB_HOST = "172.23.115.137"
DB_PORT = "50840"


# Connecting to PostgreSQL DBMS
connection = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
cur = connection.cursor()

cur.execute('''SELECT * FROM final''')
table = cur.fetchall()


def noun_insertion():
    insert_true = "UPDATE final SET contains_noun = true WHERE id=%s"
    insert_false = "UPDATE final SET contains_noun = false WHERE id=%s"
    for row in table:
        # to make sure we only accept nouns longer than 2 characters
        if regex.search('\t[a-zA-Z][a-zA-Z][a-zA-Z]+ NOUN', row[7]):
            cur.execute(insert_true, (row[0],))
            print("inserted true at " + str(row[0]))
        else:
            cur.execute(insert_false, (row[0],))
            print("inserted false at " + str(row[0]))
    connection.commit()


def verb_insertion():
    insert_true = "UPDATE final SET contains_verb = true WHERE id=%s"
    insert_false = "UPDATE final SET contains_verb = false WHERE id=%s"
    for row in table:
        if regex.search('\t[a-zA-Z][a-zA-Z][a-zA-Z]+ VERB', row[7]):
            cur.execute(insert_true, (row[0],))
            print("inserted true at " + str(row[0]))
        else:
            cur.execute(insert_false, (row[0],))
            print("inserted false at " + str(row[0]))
    connection.commit()


def adj_insertion():
    insert_true = "UPDATE final SET contains_adj = true WHERE id=%s"
    insert_false = "UPDATE final SET contains_adj = false WHERE id=%s"
    for row in table:
        if regex.search('\t[a-zA-Z][a-zA-Z][a-zA-Z]+ ADJ', row[7]):
            cur.execute(insert_true, (row[0],))
            print("inserted true at " + str(row[0]))
        else:
            cur.execute(insert_false, (row[0],))
            print("inserted false at " + str(row[0]))
    connection.commit()


def get_fun_ids() -> dict:
    """:returns: a dictionary with all ids that are sfw"""
    ids = dict()
    with open("../data_files/tweets_filtered_profanity_fun.csv") as infile:
        reader = csv.reader(infile)
        next(reader)  # skip header
        for line in reader:
            ids[line[0]] = 0
    return ids


def sfw_insertion():
    insert_true = "UPDATE final SET is_sfw = true WHERE id=%s"
    insert_false = "UPDATE final SET is_sfw = false WHERE id=%s"
    ids = get_fun_ids()
    for row in table:
        if str(row[0]) in ids:
            cur.execute(insert_true, (row[0],))
            print("inserted true at " + str(row[0]))
        else:
            cur.execute(insert_false, (row[0],))
    connection.commit()


# noun_insertion()
# verb_insertion()
# adj_insertion()
# sfw_insertion()

cur.close()
connection.close()
