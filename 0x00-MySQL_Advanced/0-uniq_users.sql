-- create a table users
-- Create table users if it does not exist
CREATE TABLE IF NOT EXISTS users (
	-- id: integer, never null, auto increment, and primary key
	id INT AUTO_INCREMENT PRIMARY KEY,
    	-- email: string (255 characters), never null, and unique
    	email VARCHAR(255) NOT NULL UNIQUE,
    	-- name: string (255 characters)
    	name VARCHAR(255)
);

