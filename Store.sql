"#CREATION DE MA DATABASE"

mysql> CREATE DATABASE store;

mysql> use store;

mysql> create table category (
    -> id int not null auto_increment primary key,
    -> nom varchar(255) );
Query OK, 0 rows affected (0.02 sec)

mysql> ALTER TABLE product
    -> ADD price int;
Query OK, 0 rows affected (0.02 sec)

ysql> create table category (
    -> id int not null auto_increment primary key,
    -> nom varchar(255) );
Query OK, 0 rows affected (0.02 sec)

mysql> insert into category (nom)
    -> Values
    -> ('Jeux videos'),
    -> ('Produit derives'),
    -> ('Occasion');
Query OK, 3 rows affected (0.01 sec)

mysql> INSERT INTO product (nom, description, quantity, id_category, price)
    -> VALUES
    -> ('Mario Kart', 'jeux de course', '10', '1', '30'),
    -> ('Tekken 8', 'jeux de combat', '10', '1', '60'),
    -> ('Pokemon Ecarlate', 'jeux d aventure', '10', '1', '40'),
    -> ('Lego Mario', 'jouet Mario', '20', '2', '15'),
    -> ('Figurine Tekken', 'jouet tekken', '20', '2', '25'),
    -> ('Carte Pokemon' , 'jeu de carte', '30', '2', '10'),
    -> ('Mario Kart', 'jeux de course', '5', '3', '15'),
    -> ('Tekken 8', 'jeux de combat', '5', '3', '30'),
    -> ('Pokemon Ecarlate', 'jeux d aventure', '5', '3', '20');
Query OK, 9 rows affected (0.01 sec)
Records: 9  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM product;
+----+------------------+-----------------+----------+-------------+-------+
| id | nom              | description     | quantity | id_category | price |
+----+------------------+-----------------+----------+-------------+-------+
|  3 | Mario Kart       | jeux de course  |       10 |           1 |    30 |
|  4 | Tekken 8         | jeux de combat  |       10 |           1 |    60 |
|  5 | Pokemon Ecarlate | jeux d aventure |       10 |           1 |    40 |
|  6 | Lego Mario       | jouet Mario     |       20 |           2 |    15 |
|  7 | Figurine Tekken  | jouet tekken    |       20 |           2 |    25 |
|  8 | Carte Pokemon    | jeu de carte    |       30 |           2 |    10 |
|  9 | Mario Kart       | jeux de course  |        5 |           3 |    15 |
| 10 | Tekken 8         | jeux de combat  |        5 |           3 |    30 |
| 11 | Pokemon Ecarlate | jeux d aventure |        5 |           3 |    20 |
+----+------------------+-----------------+----------+-------------+-------+
9 rows in set (0.00 sec)

mysql> SELECT * FROM category;
+----+-----------------+
| id | nom             |
+----+-----------------+
|  1 | Jeux videos     |
|  2 | Produit derives |
|  3 | Occasion        |
+----+-----------------+
3 rows in set (0.00 sec)

mysql>