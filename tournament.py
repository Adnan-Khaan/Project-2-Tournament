#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"): 
    try:
        db = psycopg2.connect("dbname={}".format(database_name))  # Connect to the PostgreSQL database.  Returns a database connection.
        dbcursorsor=db.cursor() # Create a cursor connecton
        return(db,dbcursorsor)
    except:
        print("Experiencing problems with DATABASE")

def deleteMatches():
    db,dbcursor = connect()  
    # Create a database connection by calling connect() that return a object
    dbcursor.execute('delete from matches;')
    # Executing SQL query using the connection
    db.commit()
    # Calling commit() to finalise the changes
    db.close()
    # Closing the connections.


def deletePlayers():
    db,dbcursor = connect()
    dbcursor.execute('DELETE from players')
    db.commit()
    db.close()


def countPlayers():
    db,dbcursor = connect()
    dbcursor.execute('select count(*) from players') 
    # Counting the total number of plyers in Players table.
    value = dbcursor.fetchone()
    return int(value[0])  
    # int()funtion to change the data type to integer.
    db.close()


def registerPlayer(name):
    db,dbcursor = connect()
    dbcursor.execute('INSERT INTO players(name) VALUES(%s)', (name, )) 
    db.commit()
    db.close()


def playerStandings():
    db,dbcursor = connect()
    dbcursor.execute('SELECT * FROM player_standings')
    standings = dbcursor.fetchall()
    return standings


def reportMatch(winner, loser):
    db,dbcursor = connect()
    dbcursor.execute('INSERT INTO matches(winner,loser)  VALUES(%s,%s)',
                  (winner, loser))
    db.commit()
    db.close()


def swissPairings():
    swisspair=[]
    standings = playerStandings()
    while (len(standings)%2)==0: # To check the even number of players for pairing.
        for player1, player2 in zip(standings[0::2],standings[1::2]): #Spliting the players in to two lists player1 and player2
            swisspair.append((player1[0],player1[1],player2[0],player2[1]))# Making pairs from the above list and saving them into swisspair
         
        return swisspair # Returning the list of tuples. 
