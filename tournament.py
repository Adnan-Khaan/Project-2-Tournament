#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""

    return psycopg2.connect('dbname=tournament')


def deleteMatches():
    db = connect()  
    # Create a database connection by calling connect() that return a object
    dbcur = db.cursor()
    # Create a cursor connecton.
    dbcur.execute('delete from matches;')
    # Executing SQL query using the connection
    db.commit()
    # Calling commit() to finalise the changes
    db.close()
    # Closing the connections.


def deletePlayers():
    db = connect()
    dbcur = db.cursor()
    dbcur.execute('DELETE from players')
    db.commit()
    db.close()


def countPlayers():
    db = connect()
    dbcur = db.cursor()
    dbcur.execute('select count(*) from players') 
    # Counting the total number of plyers in Players table.
    value = dbcur.fetchone()
    return int(value[0])  
    # int()funtion to change the data type to integer.
    db.close()


def registerPlayer(name):
    db = connect()
    dbcur = db.cursor()
    dbcur.execute('INSERT INTO players(name) values(%s)', (name, ))
    db.commit()
    db.close()


def playerStandings():
    db = connect()
    dbcur = db.cursor()
    sql = """select playerwins.id,playerwins.name,playerwins.wins,
             playermatches.match from playerwins left join playermatches
             on playerwins.id=playermatches.id order by wins desc"""
    dbcur.execute(sql)
    standings = dbcur.fetchall()
    return standings


def reportMatch(winner, loser):
    db = connect()
    dbcur = db.cursor()
    dbcur.execute('INSERT INTO matches(winner,loser) values(%s,%s)',
                  (winner, loser))
    db.commit()
    db.close()


def swissPairings():
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    [name1, name2, name3, name4] = [row[1] for row in standings]
    swisspair = [(id1, name1, id2, name2), (id3, name3, id4, name4)]
    return swisspair