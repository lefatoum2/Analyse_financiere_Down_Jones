# Analyse_financiere_Down_Jones

## Création d'un docker mysql 

```
docker run  --name downjones -p 3300:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql:5.7
```

## Lancer la commande bash du docker
```
docker exec -t -i downjones /bin/bash
```

## Lancer mysql

```
mysql -uroot -ppassword
```

## Création de table
```
USE database_name;
```

```
CREATE TABLE table_name (
            
);

```
## Charger les données csv dans MySql

```
LOAD DATA INFILE '/home/export_file.csv'
INTO TABLE table_name
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;
```
## Le choix de nos outils technologiques

### MySql

Les requêtes SQL ont la particularité de pouvoir être transformé en DataFrame en utilsant la bibliothèque de Pandas. C'est idéal lorsqu'on possède beaucoup de données à traiter et visualiser des graphiques rapidement.

### Streamlit

Comme son slogan le dit : "c'est le plus rapide chemin pour construire et partager  de la Data.

### Plotly.Express

Plotly.express est une biblithèque qui se veut que plus concis que Plotly lui-même qui possédait déjà moins de contraintes que ses concurrents. La courbe d'apprentissage est assez faible.
