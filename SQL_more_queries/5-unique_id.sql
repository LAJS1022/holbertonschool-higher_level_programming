-- 5. Unique ID
-- Script that creates the table unique_id on your MySQL server
-- The table must have:
--   id INT with a default value of 1 and must be UNIQUE
--   name VARCHAR(256)
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
