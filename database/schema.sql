CREATE DATABASE UrbanSense
USE UrbanSense;
CREATE TABLE Locations(
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    area_name VARCHAR(100),
    city VARCHAR(100),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);
CREATE TABLE Env_Data(
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    location_id INT,
    aqi INT,
    pm25 FLOAT,
    pm10 FLOAT,
    temperature FLOAT,
    humidity FLOAT,
    recorded_at DATETIME,
    FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);
