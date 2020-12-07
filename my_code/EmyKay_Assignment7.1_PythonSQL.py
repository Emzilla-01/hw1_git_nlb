# -*- coding: utf-8 -*-
"""
Emy Kay's code

# =============================================================================
DB CONNECTIVITY
Create a table to store detail about books to be given out on rental basis.  The table should maintain the inventory ie number of copies available of a particular book.  Upon giving it out to a customer, on rent, the number of copies need to get updated 

Sample data

Book Title  Copies 
------------------------
Harry potter  30
Iron man        15


Provide a menu like 

1.	Add a new book
2.	Issue book on rental
3.	Check no of copies available
4.	Exit

Each menu item should be operational

For option 2, while issuing the book, we need to check if the book is available and take action accordingly.  That is , in case the book is not on the list , then appropriate message needs to be show.

Just do the updating of the number of copies post issue of the book.  This is enough
# =============================================================================

Created on Thu Dec  3 16:05:19 2020
@author: emy
"""
import mysql.connector
host="localhost"
user="root"
password=''
# db="cakes"
flatten = lambda l : [item for sublist in l for item in sublist] # flatten([[1,2],[3],[4,[5]]])

# =============================================================================
# table data
# =============================================================================
new_dbname="library"
dbname="library"
library_init_script_sql=r"""..."""#executing entire db init script from inside python is failing silently dunno why... meantime script is inside 7_1_library_db_init.sql
with open("7_1_library_db_init.sql", 'rt', encoding='utf-8') as textfile:
        library_init_script_sql = textfile.read()
library_init_script_sql=library_init_script_sql.replace("\n", "")
library_init_script_sql=library_init_script_sql.replace("\t", "")
library_init_script_sql=library_init_script_sql.strip()

schema_enduser_description = """description of tables:
CUST - customer data
TITLE - the production run of a certain book
COPY - an instance of TITLE in library inventory
RENTAL - customer rental of a COPY
CHECKIN - customer return of RENTAL"""
# =============================================================================
#utility functions for db initialization and script development
# =============================================================================
# def execute_sql_statement_get_external(sql_st):
#     mydb = mysql.connector.connect(host=host, user=user, password=password)
#     mycursor  = mydb.cursor()     
#     mycursor.execute(sql_st)
#     data = mycursor.fetchall()
#     mydb.close()
#     return(data)

# def execute_sql_statement_commit_external(sql_st, multi=True):
#     mydb = mysql.connector.connect(host=host, user=user, password=password)# db=db)
#     mycursor  = mydb.cursor()     
#     mycursor.execute(sql_st, multi=multi)
#     mydb.commit()    
#     mydb.close()
#     return()

# =============================================================================
class LibraryTerminal():
    def __init__(self, db_obj):
        self.db = db_obj
        self.cursor = self.db.cursor()
        print("*"*20+f"\nWelcome to LibraryTerminal\nusing database: {self.db._database}\nas user: {self.db._user}")
        print("*"*20+"\n"+schema_enduser_description+"\n"+"*"*20)
        
    def execute_statement_commit(self, sql_st):
        self.cursor.execute(sql_st)
        self.db.commit()
        
    def execute_statement_get(self, sql_st):
        self.cursor.execute(sql_st)
        data=self.cursor.fetchall()
        return(data)
    
    def get_avail_copies(self):
        titleId_input = int(input("enter titleId"))
        copyId_q = self.execute_statement_get(f"""select copyId from copy
                               where titleId={titleId_input}
                               and checkedIn = True""")
        print(f"{len(copyId_q)} available")
        print(f"copyIds are: {', '.join([str(r[0]) for r in copyId_q])}")
        

    def non_handler(_j):
        return("pass")
    
    def add_data(self, tablename, cols_display, db_cols,
                 check_func, check_flag=False, post_insert_handler=non_handler):
        #title_cols_display = ["Title Name", "Author", "Publication Year", "Publisher", "Description"]
        # db_cols = ['titleName', 'author', 'titleYear', 'publisher', 'titleDesc']
        print("*"*20+f"\nwelcome to add {tablename} menu")
        new_data=list()
                
        input_buf=''
        # input_flag=True
        i=0
        while True:
            if i == len(cols_display):
                input_buf=input(f"your selection: {list(zip(cols_display, new_data))}\nenter *y to add title or any other key to quit\n")
                if input_buf.lower().strip() in ["*y", "y"]:
                    if check_flag:
                        check = check_func(new_data[-1])
                        print(f"check is {check}")
                        if not check[0]:
                            print(check[1])
                            print(f"cancelling add {tablename}\n")                    
                            return()
                        else:
                            db_cols.append(check[1])
                            new_data.append(str(check[2]))
                            print(f"db_cols:{db_cols}")
                            print(f"new_data:{new_data}")
                            print(f"tablename:{tablename}")
                            #insert copyId, copyId colname 
                            #       into db_cols & new_data
                    print(f"inserting new record {list(zip(cols_display, new_data))} to {tablename} table\n")
                    sql_st=f"""insert into {tablename} {str(tuple(db_cols)).replace("'", '')}
                        values {tuple(new_data)};"""
                    self.execute_statement_commit(sql_st)
                    post_insert_handler(self, str(check[2]))
                    
                else:
                    print(f"cancelling add {tablename}\n")                    
                return()
            input_buf=input(f"Please enter {cols_display[i]} or '*q' to quit\n")
            if input_buf.lower() == "*q":
                print(f"cancelling add {tablename}\n")
                return()
            else:
                new_data.append(input_buf)
                i+=1
            
    def add_title(self):
        tablename = "title"
        cols_display = ["Title Name", "Author", "Publication Year", "Publisher", "Description"]
        db_cols = ['titleName', 'author', 'titleYear', 'publisher', 'titleDesc']
        def check_func():
            return(True, 'no problem')
        def post_insert_handler(_j):
            print(f"successful insert on {tablename}")
        self.add_data(tablename, cols_display, db_cols, check_func, check_flag=False)
        return()
        
    def add_rental(self):
        tablename = "rental"
        cols_display = ["Customer ID", 'Title ID']
        db_cols = ['custId', 'titleId']
        def check_func(titleId):
            copyId_q = self.execute_statement_get(f"""select copyId from copy
                                           where titleId={titleId}
                                           and checkedIn = True""")
            if copyId_q == []:
                return(False, Exception("No copy available for this title"))
            else:
                return (True, "copyId", copyId_q[-1][0]) # returns (True, colname, copyId)
        
        def rental_handler(self, _j):
            stmnt=f"""update copy
            set checkedIn = False
            where copyId={_j}"""
            print(stmnt)
            self.execute_statement_commit(stmnt)
        
        
        self.add_data(tablename, cols_display, db_cols, check_func, check_flag=True, post_insert_handler=rental_handler)
        print(f"attempted add data on {tablename}")
        
    def main_menu(self):
        print("*"*20)
        print("Welcome to LibraryTerminal main menu")
        while True:
            try:
                main_menu_input=int(input("1.	Add a new book\n2.	Issue book on rental\n3.	Check no of copies available\n4.	Exit\n"))
                if main_menu_input == 4:
                    print("ending session")
                    return(0)
                if main_menu_input == 1:
                    self.add_title()
                if main_menu_input == 2:
                    self.add_rental()
                if main_menu_input == 3:
                    self.get_avail_copies()
            except ValueError as e:
                print("invalid input")
            finally:
                self.db.close()

if __name__ == "__main__":
    # execute_sql_statement_commit_external(library_init_script_sql) # Not working inside python.. don't know why
    l = LibraryTerminal(  mysql.connector.connect(host=host, user=user, password=password, db=dbname) ) 
    l.main_menu()
    #l.execute_statement_get("select * from copy")
