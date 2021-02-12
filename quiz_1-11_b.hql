use hivetestDB;

select roles.dept, roles.grade from emps;

select demographic.sex, demographic.age from emps;

select speciality from emps where speciality['DB'] is not null;


create table if not exists ny_emps (ename string,
location STRUCT<city:string, region:string>,
demographic STRUCT<sex:string, age:int>,
speciality MAP<string, int>,
roles ARRAY <STRUCT<dept:string, grade:string>>)
row format delimited
fields terminated by '|'
collection items terminated by ','
map keys terminated by ':';

insert into ny_emps select * from emps where location.city='New York';

select * from ny_emps;

select demographic.sex, count(ename), avg(demographic.age) from emps group by demographic.sex;

