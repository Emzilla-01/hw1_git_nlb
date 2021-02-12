employee = LOAD 'hdfs://localhost:9000/pig/pig_data.json' using JsonLoader('id:chararray, 
f_name:chararray, l_name:chararray, gender: chararray, salary:int, city:chararray,
country:chararray');

/* dump employee;
*/
filter_f = filter employee by gender == 'Female';
filter_m = filter employee by gender == 'Male';


filter_1 = filter employee by country matches 'B.*';

filter_2 = filter employee by country in ('United States', 'China');

/*
store filter_f into '/pig/female_employee';
store filter_m into '/pig/male_employee';

dump filter_1;
dump filter_2;

limit_m = LIMIT filter_m 10;
dump limit_m;
*/

SPLIT employee into emp_hisal if $4 >= 50000,
		     emp_losal if $4 < 50000;

dump emp_hisal;

dump emp_losal;

