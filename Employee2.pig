employee = LOAD 'hdfs://localhost:9000/pig/pig_data.json' using JsonLoader('id:chararray, 
f_name:chararray, l_name:chararray, gender: chararray, salary:int, city:chararray,
country:chararray');


/*
group_1 = GROUP employee BY gender;

filter_1 = filter employee by $6 == 'United States';
group_2 = GROUP filter_1 BY (country, gender);

dump group_2;
*/

employee_1 = FOREACH employee GENERATE f_name, gender, salary;

dump employee_1;

