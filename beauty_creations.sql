CREATE DATABASE IF NOT EXISTS beauty_creations;
USE beauty_creations;
CREATE TABLE accessories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price DECIMAL(10, 2),
    price_zscore FLOAT
);

CREATE TABLE bundles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price DECIMAL(10, 2),
    price_zscore FLOAT
);

CREATE TABLE collabs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price DECIMAL(10, 2),
    price_zscore FLOAT
);

