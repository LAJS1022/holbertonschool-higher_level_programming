-- 3. Always a name
-- Script that creates the table force_name on your MySQL server
-- The table must have:
--   id INT
--   name VARCHAR(256) which cannot be NULL
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
