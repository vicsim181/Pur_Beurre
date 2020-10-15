CREATE DATABASE maindb CHARACTER SET 'utf8';

USE maindb;

CREATE TABLE Products (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name_product VARCHAR(80) NOT NULL,
    id_category SMALLINT NOT NULL,
    name_category VARCHAR(40) NOT NULL,
    global_nutri_score CHAR(1) NOT NULL,
    description_product TEXT NOT NULL,
    link_off TEXT NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Favorites (
    request_number SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    id_product_replaced SMALLINT NOT NULL,
    name_product_replaced VARCHAR(80) NOT NULL,
    global_nutri_score_replaced CHAR(1) NOT NULL,
    id_product_replacing SMALLINT NOT NULL,
    name_product_replacing VARCHAR(80) NOT NULL,
    global_nutri_score_replacing CHAR(1) NOT NULL,
    selling_places_replacing_product VARCHAR(80) NOT NULL,
    date_request DATETIME NOT NULL,
    PRIMARY KEY (request_number)
)
ENGINE=INNODB;

CREATE TABLE Selling (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    selling_place_name VARCHAR(80) NOT NULL,
    city_name VARCHAR(60) NOT NULL,
    available_products TEXT NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE Category (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
)
ENGINE=INNODB;



