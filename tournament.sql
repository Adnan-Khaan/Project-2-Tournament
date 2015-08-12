-- TABLE definitions for the tournament project.

DROP DATABASE IF EXISTS tournament; --Deleting the database if it already exist.
CREATE database tournament;-- Creating the database.	
\c tournament;
DROP TABLE IF EXISTS matches;-- Deleting the TABLE if it's already exist.
DROP TABLE IF EXISTS players; 
CREATE TABLE players(
                    Id SERIAL PRIMARY KEY,
                    name TEXT
                    ); -- Creating the Players TABLE and defining the fields ID as PRIMARY KEY  and Name.
CREATE TABLE matches(
                    mid SERIAL PRIMARY KEY,
                    winner INT DEFAULT NULL REFERENCES players(Id),
                    loser INT DEFAULT NULL REFERENCES players(Id)
                    );-- Creating the matches TABLE and defining the fields Mid as PRIMARY KEY  and winner and loser, defining the references to players TABLE .
DROP VIEW IF EXISTS player_matches; -- Deleting the VIEW if it's already exist.
DROP VIEW IF EXISTS player_wins;    -- Deleting the VIEW if it's already exist.	
CREATE VIEW player_wins AS
                    SELECT players.id,players.name,
                    COUNT(matches.winner) AS wins 
                    FROM players LEFT JOIN matches 
                    ON players.id= matches.winner 
                    GROUP BY players.id 
                    ORDER BY players.id;
                    -- Creating the VIEW playersmates that will show the all the players with their standings .
CREATE VIEW player_matches AS 
                    SELECT players.id,
                    COUNT(matches.mid) AS match 
                    FROM players 
                    LEFT JOIN matches 
                    ON matches.winner = players.id 
                    OR matches.loser=players.id GROUP BY players.id;
                    -- Creating the VIEW playmatches which will show all the player with the number of matches they played. 
CREATE VIEW player_standings AS
                    SELECT player_wins.id,
                    player_wins.name,
                    player_wins.wins,
                    player_matches.match
                    FROM player_wins LEFT JOIN player_matches
                    ON player_wins.id=player_matches.id 
                    ORDER BY wins desc;
                    -- Create the VIEW player_standing will show all the player with their wins and matches in an order. 