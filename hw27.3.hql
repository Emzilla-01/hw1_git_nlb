set hive.exec.dynamic.partition = true;
set hive.exec.dynamic.partition.mode = nonstrict;
set hive.enforce.bucketing = true;

create database if not exists hw273_db;

use hw273_db;

drop table if exists emp;

create external table if not exists emp_ext (empid int, empname string, email string, gender string, salary int, city string, country string, tz string, lor string, doj timestamp)
row format delimited
fields terminated by ',';

load data local inpath '/home/hadoop/data/hw27.3.csv'
overwrite into table emp_ext;


drop table if exists emp_ext_part_country;

create table emp_ext_part_country (empid int, empname string, email string, gender string, salary int, city string, tz string, lor string, doj timestamp)
partitioned by (country string)
row format delimited
fields terminated by ',';


insert overwrite table emp_ext_part_country 
partition(country)
select empid, empname, email, gender, salary, city, tz, lor, doj, country from emp_ext;



drop table if exists emp_ext_part_country_city;

create table emp_ext_part_country_city (empid int, empname string, email string, gender string, salary int, tz string, lor string, doj timestamp)
partitioned by (country string, city string)
row format delimited
fields terminated by ',';


insert overwrite table emp_ext_part_country_city
partition(country, city)
select empid, empname, email, gender, salary, tz, lor, doj, country, city from emp_ext;




!echo ***************************************************\n;

!echo "table sample";
select * from emp_ext_part_country_city tablesample (5 rows);

!echo ***************************************************\n;

!echo "employees per country";
select count(empid), country from emp_ext_part_country_city  group by country;
!echo ***************************************************\n;

!echo "total of each gender";
select count(empid), gender from emp_ext_part_country_city  group by gender;
!echo ***************************************************\n;

!echo "average salary by country";
select avg(salary), country from emp_ext_part_country_city  group by country;
!echo ***************************************************\n;


