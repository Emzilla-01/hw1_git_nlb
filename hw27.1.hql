
set hive.server2.logging.operation.level=NONE; -- not working, trying to suppress warnings in console output

create database if not exists hw271_db;

use hw271_db;

drop table if exists emp;

create external table if not exists emp (empid int, empname string, email string, gender string, salary int, city string, country string, tz string)
row format delimited
fields terminated by ',';

load data local inpath '/home/hadoop/data/empdb_27.1.csv'
overwrite into table emp;

!echo ***************************************************\n;

!echo table sample;
select * from emp tablesample (5 rows);

!echo ***************************************************\n;

!echo employees per country;
select count(empid), country from emp group by country;
!echo ***************************************************\n;

!echo average sal by each gender;
select avg(salary), gender from emp group by gender;
!echo ***************************************************\n;

!echo "average salary by country";
select avg(salary), country from emp group by country;
!echo ***************************************************\n;

!echo variance of salary by country;
select variance(salary), country from emp group by country;
!echo ***************************************************\n;

!echo histogram of salary (global);
select histogram_numeric(salary, 10) from emp;

!echo ***************************************************\n;
