create database if not exists employeeDB;

use employeeDB;

drop table if exists employee_te;

create external table if not exists employee_t (empid int, firstname string, lastname string, email string, gender string, salary int, country string)
row format delimited
fields terminated by ',';

load data local inpath '/home/hadoop/MOCK_DATA.csv'
overwrite into table employee_t;

select firstname, salary from employee_t order by salary desc limit 20;
