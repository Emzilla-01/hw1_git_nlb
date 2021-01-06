create database if not exists partitiondb;

use partitiondb;

drop table if exists employee_t;

create external table if not exists employee_t (empid int, empname string, email string, gender string, salary int, city string, country string)
row format delimited
fields terminated by ',';

load data local inpath '/home/hadoop/Downloads/Employee.csv'
overwrite into table employee_t;

SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

drop table if exists emppart_table;

create external table if not exists emppart_table (empid int, empname string, email string, gender string, salary int, city string)
partitioned by (country string)
row format delimited
fields terminated by ',';

INSERT OVERWRITE TABLE emppart_table
PARTITION (country)
SELECT * FROM employee_t;