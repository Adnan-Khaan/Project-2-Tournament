-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like


Drop database IF exists tournament; --Deleting the database if it already exist.
create database tournament;-- Creating the database.	
	\c tournament;
	Drop table IF exists matches;-- Deleting the Table if it's already exist.
	Drop table IF exists players; 
	Create table players(Id serial primary key, name text); -- Creating the Players table and defining the fields ID as primary key  and Name.
 	Create table matches(mid serial primary key, winner int Default Null references players(Id), loser int Default Null references players(Id));
    -- Creating the matches table and defining the fields Mid as primary key  and winner and loser, defining the references to players table .
    Drop VIEW if exists playermatches; -- Deleting the View if it's already exist.
    Drop VIEW if exists playerwins;	   -- Deleting the View if it's already exist.	
    Create view playerwins as select players.id,players.name, count(matches.winner) as wins from players left join matches on players.id= matches.winner group by players.id order by players.id;
    -- Creating the view playersmates that will show the all the players with their standings .
    Create view playermatches as select players.id, count(matches.mid) as match from players left join matches on matches.winner = players.id OR matches.loser=players.id group by players.id;  
    -- Creating the view playmatches which will show all the player with the number of matches they played. 