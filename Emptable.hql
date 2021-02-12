create database if not exists employeeDB;

use employeeDB;

drop table if exists emptable;

create table if not exists emptable (empid int, firstname string, lastname string, email string, gender string, salary int, country string)
row format delimited
fields terminated by ',';

load data local inpath '/home/hadoop/MOCK_DATA.csv'
overwrite into table emptable;

select firstname, salary from emptable order by salary desc limit 20;
