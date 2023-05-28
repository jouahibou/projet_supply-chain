-- Active: 1684518215732@@127.0.0.1@3306@database
CREATE TABLE Entreprises (
    Nom Varchar(255),
    Note DECIMAL(5,2),
    Nombre_avis INT,
    Avis_excelents DECIMAL(5,0),
    Domaine VARCHAR(255)
);


LOAD DATA LOCAL INFILE 'trustpilot_data1.csv'
INTO TABLE Entreprise
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

SHOW VARIABLES LIKE 'secure_file_priv';
select * from Entreprise ;
