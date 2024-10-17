-- A script that creates a table 'users' with the following requirements:
-- attributes:
--    `id`: integer, never null, auto increment and primary key
--    `email`: string (255 characters), never null and unique
--    `name`: string (255 characters)
-- If the table already exists, it doesn not fail
-- The script can be executed on any database

-- creates the table users
CREATE TABLE IF NOT EXISTS users(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
);
