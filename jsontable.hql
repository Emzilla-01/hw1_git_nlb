create database if not exists jsondb;

use jsondb;

create table if not exists json_table(json_str string);

load data local inpath '/home/hadoop/MOCK_DATA.json' into table json_table;

select get_json_object(json_str, '$.first_name') as first_name, get_json_object(json_str, '$.salary') as salary from json_table where get_json_object(json_str, '$.salary') > 50000 limit 20;
