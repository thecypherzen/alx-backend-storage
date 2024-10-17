-- Creates the table `users` with the following requirements:
-- These attributes:
--     1. id, integer, never null, auto increment and primary key
--     2. email, string (255 characters), never null and unique
--     3. name, string (255 characters)
--     4. country, enumeration of countries: US, CO and TN,
--        never null (= default will be the first element of
--        the enumeration, here US)
-- If table exists, the code doesn't fail
-- The script can be executed on any database

-- creates the table users
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') DEFAULT 'US'
);
