
from flask import Flask, render_template
import psycopg2
from blank_generation import create_blank
from scoring import get_points

app = Flask(__name__)


def connect_db():
    DB_NAME = "team_f_db"
    DB_USER = "postgres"
    DB_PASS = "d3e8db4016b1e148da8a12e4f361be44"
    DB_HOST = "172.23.115.137"
    DB_PORT = "50840"
    connection = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

    return connection


@app.route('/')
def standard_website():
    return render_template('templates/home.html')


@app.route('/nouns')
def get_noun():
    cursor = connect_db()
    rdm = cursor().execute('''
        SELECT * FROM tweets
        ORDER BY RANDOM()
        LIMIT 1''')
    create_blank('NOUN', rdm[1], rdm[3])


@app.route('/proper-nouns')
def get_proper():
    cursor = connect_db()
    rdm = cursor().execute('''
        SELECT * FROM tweets
        ORDER BY RANDOM()
        LIMIT 1''')
    create_blank('PROPN', rdm[1], rdm[3])


@app.route('/verbs')
def get_verb():
    cursor = connect_db()
    rdm = cursor().execute('''
        SELECT * FROM tweets
        ORDER BY RANDOM()
        LIMIT 1''')
    create_blank('VERB', rdm[1], rdm[3])


@app.route('/adjectives')
def get_adjective():
    cursor = connect_db()
    rdm = cursor().execute('''
        SELECT * FROM tweets
        ORDER BY RANDOM()
        LIMIT 1''')
    create_blank('ADJ', rdm[1], rdm[3])

