create database if not exists complexDb;

use complexDB;

drop table if exists complex_table;

create table if not exists complex_table(
empid int,
fullname map<string, string>,
location struct<country:string, zip:int>,
skills array<string>
)

row format delimited
fields terminated by '\t'
collection items terminated by ','
map keys terminated by ':'
;

LOAD DATA LOCAL INPATH '/home/hadoop/complex_data_type.txt'
OVERWRITE INTO TABLE complex_table;

select * from complex_table;
