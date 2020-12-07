# -*- coding: utf-8 -*-
"""

Created on Thu Dec  3 16:05:19 2020
@author: emy
"""
import mysql.connector
host="localhost"
user="root"
password=''
db="cakes"
flatten = lambda l : [item for sublist in l for item in sublist] # flatten([[1,2],[3],[4,[5]]])

def execute_sql_statement(sql_st):
    mydb = mysql.connector.connect(host=host, user=user, password=password)# db=db)
    mycursor  = mydb.cursor()     
    mycursor.execute(sql_st)
    # mycursor.execute(output)
    data = mycursor.fetchall()
    # mydb.commit()
    mydb.close()
    return(data)

all_schemas_sql = """select schema_name as database_name
from information_schema.schemata
order by schema_name;"""

get_all_tables_from_schema = lambda __s__ : rf"""SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='{__s__}'"""

if __name__ == "__main__":    
    all_schemas_result=flatten(execute_sql_statement(all_schemas_sql))    
    x = list(zip(all_schemas_result, [execute_sql_statement(get_all_tables_from_schema(__s__)) for __s__ in all_schemas_result]))
    [print(i) for i in x]
    
    
    