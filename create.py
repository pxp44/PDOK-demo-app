# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys

import sqlite3


def create_db(pgConn):
    if pgConn is None:
        conn = sqlite3.connect('request.db')
    else:
        conn = pgConn
    c = conn.cursor()

    if pgConn is None:
        c.execute('''CREATE TABLE IF NOT EXISTS requests
             (path text, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);''')
        c.execute('''CREATE TABLE IF NOT EXISTS datasets
             (privateKey text, publicKey text, activated integer,
             email text, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);''')
        c.execute('''CREATE TABLE IF NOT EXISTS d_d89d5ee2d34711e59d78bcaec5c2cce2
             (uuid text, privUuid text, ip text,
             Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, location text);''')
    else:
        c.execute('''CREATE TABLE IF NOT EXISTS requests
             (nr bigserial PRIMARY KEY, path text, Timestamp timestamp DEFAULT CURRENT_TIMESTAMP);''')
        c.execute('''CREATE TABLE IF NOT EXISTS datasets
             (privateKey text PRIMARY KEY, publicKey text, activated integer,
             email text, Timestamp timestamp DEFAULT CURRENT_TIMESTAMP);''')
        c.execute('''CREATE TABLE IF NOT EXISTS d_d89d5ee2d34711e59d78bcaec5c2cce2
             (uuid text, privUuid text PRIMARY KEY, ip text,
             Timestamp timestamp DEFAULT CURRENT_TIMESTAMP, location text);''')

    try:
        c.execute('''INSERT INTO datasets (privateKey, publicKey, activated)
             VALUES('d89d5ee2-d347-11e5-9d78-bcaec5c2cce2', 'd89d5ee2-d347-11e5-9d78-bcaec5c2cce2', 1);''')
    except Exception as e:
        print(e)
        print("You may ignore previous error...")
    conn.commit()
    if pgConn is None:
        conn.close()
