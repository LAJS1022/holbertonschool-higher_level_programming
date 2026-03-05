-- 2. Read user
-- Script that creates the database hbtn_0d_2 and the MySQL server user user_0d_2
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The password must be set to user_0d_2_pwd
-- If the database already exists, the script should not fail
-- If the user already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
