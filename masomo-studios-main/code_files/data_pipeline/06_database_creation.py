#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create database from Twitter API

# TODO: optimal final format of db : id, tweet, tweet_tagged, user_name (Maxine)

import psycopg2
import csv

DB_NAME = "team_f_db"
DB_USER = "postgres"
DB_PASS = "d3e8db4016b1e148da8a12e4f361be44"
DB_HOST = "172.23.115.137"
DB_PORT = "50840"

# Connecting to PostgreSQL DBMS
connection = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
print("Database connected successfully")

# Obtaining a DB Cursor
cursor = connection.cursor()

# to avoid confusion
cursor.execute('''DROP TABLE IF EXISTS tweets;''')

# Creation of tables
cursor.execute("""CREATE TABLE IF NOT EXISTS tweets (
id INT PRIMARY KEY,
tweet TEXT,
user_name TEXT,
tweet_tagged TEXT
);
""")

print("Table created successfully")

connection.commit()

# Insertion of data
tweets_file = csv.reader(open("../data_files/tweets_merged.csv"))
next(tweets_file)  # Skip the header row
for row in tweets_file:
    cursor.execute("""INSERT INTO tweets 
    (id, tweet, user_name, tweet_tagged)
    VALUES(%s, %s, %s, %s)""", row)

print("Data inserted successfully")


connection.commit()
connection.close()

