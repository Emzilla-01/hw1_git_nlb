set hive.exec.dynamic.partition.mode=nonstrict

create database if not exists hivetestDB;
use hivetestDB;

drop table if exists movies;
drop table if exists movies_part;

create external table if not exists movies (ix int,
title string,
year int,
rating int,
length int)
row format delimited
fields terminated by ',';

load data local inpath 'movies_data.csv'
overwrite into table movies;

create table movies_part(ix int,
title string,
year int,
length int)
PARTITIONED BY (rating int)
row format delimited
fields terminated by ','
;

INSERT OVERWRITE TABLE movies_part PARTITION(rating)
SELECT ix, title, year, length, rating from movies;

select * from movies_part;
