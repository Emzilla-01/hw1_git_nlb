create database if not exists bucketingdb;

use bucketingdb;

create external table if not exists employee_tbl(empid int, empname string, email string, gender string, salary int, city string, country string)
row format delimited
fields terminated by ','
location '/test0/';

SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.enforce.bucketing = true;

create external table if not exists bucketingtable(empid int, empname string, email string, gender string, salary int, city string)
partitioned by (country string)
clustered by (gender) into 4 buckets
row format delimited
fields terminated by ',';

insert overwrite table bucketingtable
partition (country)
select count(empid) from bucketingtable where country = "China";
