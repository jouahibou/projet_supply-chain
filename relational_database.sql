-- Active: 1684518215732@@127.0.0.1@3306@database
CREATE TABLE entreprises (
    id_entreprise INT PRIMARY KEY,
    nom_entreprise VARCHAR(255),
    note_entreprise FLOAT,
    nombre_avis INT,
    pourcentage_avis_excellents FLOAT,
    id_domaine INT,
    FOREIGN KEY (id_domaine) REFERENCES domaine(id_domaine)
);

CREATE TABLE domaines (
    id_domaine INT PRIMARY KEY,
    nom_domaine VARCHAR(255)
);

LOAD DATA LOCAL INFILE 'trustpilot_data1.csv'
INTO TABLE entreprise
FIELDS TERMINATED BY ','
IGNORE 1 ROWS
(Nom, Note, `Nombre_davis`, `Pourcentage_avis_excellents`, Domaine)
SET entreprise.id_domaine = (
  SELECT id_domaine FROM domaines 
  WHERE domaines.nom_domaine = entreprise.Domaine
);



