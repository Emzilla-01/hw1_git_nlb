create database if not exists hivetestDB;
use hivetestDB;
drop table if exists emps;
drop database hivetestDB;

CREATE DATABASE hivetestDB
COMMENT 'hivedatabase test'
WITH DBPROPERTIES ('creator' = 'Emy', 'date' = '2021-01-11');

use hivetestDB;

create external table emps (ename string,
location STRUCT<city:string, region:string>,
demographic STRUCT<sex:string, age:int>,
speciality MAP<string, int>,
roles ARRAY <STRUCT<dept:string, grade:string>>)
row format delimited
fields terminated by '|'
collection items terminated by ','
map keys terminated by ':';


load data local inpath '/home/hadoop/employee_demo.txt'
overwrite into table emps;



select * from emps;


