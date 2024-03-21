CREATE DATABASE spareshop;
USE spareshop;

CREATE TABLE user (
    id VARCHAR(100) PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE shop (
    id VARCHAR(100) PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL UNIQUE,
	shopname VARCHAR(100) NOT NULL UNIQUE, 
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

ALTER TABLE buyer
MODIFY username VARCHAR(100) NOT NULL UNIQUE,
MODIFY email VARCHAR(100) NOT NULL UNIQUE,
MODIFY password VARCHAR(100) NOT NULL,
MODIFY address VARCHAR(100) NOT NULL;
ALTER TABLE buyer
RENAME user;
ALTER TABLE user
MODIFY COLUMN id VARCHAR(100);

ALTER TABLE shop
MODIFY username VARCHAR(100) NOT NULL UNIQUE,
MODIFY email VARCHAR(100) NOT NULL UNIQUE,
MODIFY password VARCHAR(100) NOT NULL,
MODIFY address VARCHAR(100) NOT NULL;
ALTER TABLE shop
MODIFY COLUMN id VARCHAR(100);
-- March 21st, 2024 
ALTER TABLE shop
RENAME COLUMN username to user_id;
ALTER TABLE shop
ADD CONSTRAINT FK_user_id
FOREIGN KEY (user_id) REFERENCES user(id);
ALTER TABLE shop
ADD shopname VARCHAR(100);
ALTER TABLE shop
MODIFY COLUMN shopname VARCHAR(100) NOT NULL UNIQUE;


SELECT * FROM user;