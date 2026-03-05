-- 7. Cities table
-- Script that creates the database hbtn_0d_usa and the table cities
-- The table must have:
--   id INT, UNIQUE, AUTO_INCREMENT, NOT NULL, PRIMARY KEY
--   state_id INT, NOT NULL, FOREIGN KEY referencing states(id)
--   name VARCHAR(256) NOT NULL
-- If the database already exists, the script should not fail
-- If the table already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
