-- Active: 1684518215732@@127.0.0.1@3306@database
CREATE TABLE Avis (
    Nom Varchar(255),
    Note DECIMAL(5,2),
    Nombre_avis INT,
    Pourcentage_avis_excelents VARCHAR(255),
    Domaine VARCHAR(255)
);


LOAD DATA LOCAL INFILE 'trustpilot_data.csv'
INTO TABLE Avis
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

SHOW VARIABLES LIKE 'secure_file_priv';