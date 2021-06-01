#################################################################################
# TITLE:            ETL: File to SQLite3                                        #
# AUTHOR:           BASASKS                                                     #
# PYTHON VERSION:   Python 3.8.5                                                #
# USAGE:            python3 py06_sc_filesqlite.py                               #
# DEV NOTES:        1. Code includes creation of database objects               #   
#                   2. Input file is comma-delimited                            #
#                                                                               #
#################################################################################


#####   MODULES

import os
import sqlite3
from sqlite3 import Error


#####   STATIC VARIABLES

database = "/home/basasks/output/py06/woso.db"
filesource = "/home/basasks/input/py06/py06_in_woso.txt"
filetarget = "/home/basasks/output/py06/py06_out_woso.txt"
sql_ct_stage =  """create table tbl_woso_stage (
                        date varchar(100),
                        home_team varchar(100),
                        away_team varchar(100),
                        home_score varchar(100),
                        away_score varchar(100),
                        tournament varchar(100),
                        city varchar(100),
                        country varchar(100),
                        neutral varchar(100)
                    );"""
sql_ct_core =   """ create table tbl_woso_core (
                        date char(10) not null,
                        home_team varchar(50) not null,
                        away_team varchar(50) not null,
                        home_score int not null,
                        away_score int not null,
                        tournament varchar(50) not null,
                        city varchar(50) not null,
                        country varchar(50) not null,
                        neutral int not null
                    );"""
sql_inssel = """    insert into tbl_woso_core
                    select 
                        date,
                        home_team,
                        away_team,
                        cast(home_score as integer) home_score,
                        cast(away_score as integer) away_score,
                        tournament,
                        city,
                        country,
                        case neutral when 'TRUE' then 1 ELSE 0 end neutral
                    from tbl_woso_stage;
                    """
                    

##### FUNCTIONS

# CREATE SQLITE CONNECTION
def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

# CREATE TABLE
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.close()
    except Error as e:
        print(e)
                  
        
#####   MAIN PROGRAM

# DROP DATABASE IF EXISTS
if os.path.isfile(database):
    os.remove(database)
    print("Existing database removed: " + database)

# CREATE DATABASE CONNECTION
conn = create_conn(database)
print("Database created: " + database)

# CREATE TABLES IN DATABASE
with conn:
    create_table(conn, sql_ct_stage)
    print("Table created: tbl_woso_stage")
    create_table(conn, sql_ct_core)
    print("Table created: tbl_woso_core")

# INSERT DATA FROM SOURCE FILE TO STAGING TABLE
list_line = []
with open(filesource) as fs:
    next(fs)
    for line in fs:
        list_line = line.rstrip().split(",")
        try: 
            c = conn.cursor()
            c.execute('insert into tbl_woso_stage ( date, home_team, away_team, home_score, away_score, tournament, city, country, neutral ) values ( ?, ?, ?, ?, ?, ?, ?, ?, ? )', ( list_line[0], list_line[1], list_line[2], list_line[3], list_line[4], list_line[5], list_line[6], list_line[7], list_line[8] ) )
            c.close()
        except Error as e:
            print(e)
    print("Data inserted: source file to tbl_woso_stage")
    
# INSERT DATA FROM STAGING TABLE TO CORE TABLE
try: 
    c = conn.cursor()
    c.execute(sql_inssel)
    c.close()
except Error as e:
    print(e)
print("Data inserted: tbl_woso_stage to tbl_woso_core")    

# OUTPUT DATA FROM CORE TABLE TO TARGET FILE
if os.path.isfile(filetarget):
    os.remove(filetarget)
    print("Existing target file removed: " + filetarget)
fileout = open(filetarget, "w")
try: 
    c = conn.cursor()
    fulldata = c.execute('select * from tbl_woso_core;')
    rows = c.fetchall() 
    for line in rows:
        fileout.write(str(line)[1:-1] + "\n")
    c.close()
except Error as e:
    print(e)    
fileout.close()
print("Data output: tbl_woso_stage to tbl_woso_core")    

# COMMIT AND CLOSE
conn.commit()    
conn.close() 
