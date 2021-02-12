set hive.server2.logging.operation.level=NONE; -- not working, trying to suppress warnings in console output

create database if not exists hw272_db;

use hw272_db;

drop table if exists emp;

create table if not exists emp (jn string);

load data local inpath '/home/hadoop/data/hw27.2.json'
overwrite into table emp;

!echo ***************************************************\n;

!echo table sample;
select * from emp tablesample (5 rows);

!echo ***************************************************\n;

!echo employees per country;
select count( get_json_object(jn, '$.id')  ), get_json_object(jn, '$.country') as country from emp group by get_json_object(jn, '$.country');
!echo ***************************************************\n;

!echo average sal by each gender;
select avg(get_json_object(jn, '$.salary')), get_json_object(jn, '$.gender') from emp group by get_json_object(jn, '$.gender');
!echo ***************************************************\n;

!echo "average salary by country";
select avg(get_json_object(jn, '$.salary')), get_json_object(jn, '$.country') from emp group by get_json_object(jn, '$.country');
!echo ***************************************************\n;

!echo variance of salary by country;
select variance(get_json_object(jn, '$.salary')), get_json_object(jn, '$.country') from emp group by get_json_object(jn, '$.country');
!echo ***************************************************\n;

!echo histogram of salary (global);
select histogram_numeric(cast(get_json_object(jn, '$.salary') as float), 10) from emp;

!echo ***************************************************\n;
