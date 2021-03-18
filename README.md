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

```
USE database_name;

CREATE TABLE table_name (
            id INT NOT NULL AUTO_INCREMENT,
            column_1 VARCHAR(255) NOT NULL,
            column_2 DATE NOT NULL,
            column_3 DECIMAL(10 , 2 ) NULL,
            column_4 INTEGER,
            PRIMARY KEY (id)
);

LOAD DATA INFILE '/home/export_file.csv'
INTO TABLE table_name
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;
```
