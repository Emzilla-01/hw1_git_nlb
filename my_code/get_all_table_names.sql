select schema_name as database_name
from information_schema.schemata
order by schema_name;

SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='multiplex_db';

