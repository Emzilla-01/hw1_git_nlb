# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:31:15 2020
Overcomplicated example to programmatically create table and insert rows
#cakes_init.sql
# =============================================================================
drop database if exists cakes;
create DATABASE if not exists cakes;
USE cakes;
# =============================================================================
@author: emy
mysql.connector.__version__ == '2.2.9'
"""
import mysql.connector
# =============================================================================
# connection
# =============================================================================
# mydb = mysql.connector.connect(host="localhost", user="root", password='', db="cakes")
host="localhost"
user="root"
password=''
db="cakes"
# =============================================================================
# data
# =============================================================================
fieldNames_excluded_from_insert = ["cakeId"]
table_args = {"table_name":"cakes",
            "columns":[{"name": "cakeId","type": "int primary key auto_increment"},
                       {"name": "Cake_name","type": "varchar(31)"},
                       {"name": "Shape",    "type": "varchar(31)"},
                       {"name": "Flavor",   "type": "varchar(31)"},
                       ]
                }

cake_rows = [["Lamington", "Cube", "Chocolate & coconut"],
             ["Red Devil", "Cylinder", "Red beets & sin"],
             ["Pumpkin",   "Cylinder", "Actually a pie?"],
             ]
# =============================================================================
# question 1 functions
# =============================================================================
column_text_getter = lambda t_a: " ".join ([t_a.get('name'), t_a.get('type')])
column_text_getter_insert = lambda t_a: " ".join ([t_a.get('name')])
cake_row_text_getter = lambda c_r: "("+ ", ".join(["'"+ _a + "'" for _a in c_r]) +")"

def execute_sql_statement(output):
    mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
    mycursor  = mydb.cursor()     
    mycursor.execute(output)
    mydb.commit()
    mydb.close()
    
def create_table(table_args):
    output=f"create table if not exists {table_args.get('table_name')}("
    lst=[column_text_getter(c) for c in table_args.get('columns')]
    for _s in lst:
        output += _s
        if _s != lst[-1]:
            output += ","
        else:
            output += ');'
    return(output)

def insert_cake_rows(rows, table_args):
    tablename=table_args.get("table_name")
    columns= ", ".join([column_text_getter_insert(c) for c in table_args.get('columns') if column_text_getter_insert(c) not in fieldNames_excluded_from_insert])
    output=f"insert into {tablename} ({columns}) values "
    row_text_lst = [cake_row_text_getter(c_r) for c_r in rows]
    for row in row_text_lst:
        output += row
        if row == row_text_lst[-1]:
            output += "; "
        else:
            output += ", "
    return(output)
# =============================================================================
# Question 1 main
# =============================================================================
if __name__ == "__main__":
    results = list()
    create_table_statement = create_table(table_args)
    insert_rows_statement = insert_cake_rows(cake_rows, table_args)
    [results.append(r) for r in  [execute_sql_statement(create_table_statement), 
                                  execute_sql_statement(insert_rows_statement)]]        

# =============================================================================
# question 2
# =============================================================================
def search_cakes(_srch_str):   
    mydb = mysql.connector.connect(host=host, user=user, password=password, db=db)
    mycursor  = mydb.cursor()     
    select_sql = f"SELECT * FROM cakes WHERE Cake_name like '{_srch_str}'"
    mycursor.execute(select_sql)
    for row in mycursor:
        print(row)
    mydb.close()

if __name__ == "__main__":
    search_cakes("red%")
    search_cakes("%ton")
    search_cakes("pump%")

# =============================================================================
# question 3 
# =============================================================================
def count_lst_items(lst):
    count=dict()
    for n in lst:
        if n in count.keys():
            count[n]+=1
        else:
            count[n]=1
    return(count)

def count_lst_items1(lst):
    from collections import Counter
    count=Counter()
    for n in lst:
        count[n]+=1
    return(count)

if __name__ == "__main__":
    from timeit import Timer
    d = [1,2,4,1,2,3,4,5,6,4,8]
    t0 = Timer(lambda: count_lst_items(d))
    t1 = Timer(lambda: count_lst_items1(d))
    print(t0.timeit(number=1))
    print(t1.timeit(number=1))
    assert count_lst_items(d) == count_lst_items1(d)