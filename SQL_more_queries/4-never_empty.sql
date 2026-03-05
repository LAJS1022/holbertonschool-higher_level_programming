-- 4. ID can't be null
-- Script that creates the table id_not_null on your MySQL server
-- The table must have:
--   id INT with a default value of 1
--   name VARCHAR(256)
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
