# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:26:50 2018

@author: Asus
"""

import  psycopg2
import os

os.chdir(r"/home/astana/Downloads")
conn_string = "dbname='postgres' user='postgres' password='postgres' host='localhost'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
# fill in with some data
file = 'order_products.csv'
PRODUCT_ID = 'product_id'
REORDERED = 'reordered'
# reading the file
input_file = open(file, 'r')
headers = input_file.readline().strip('\n').split(",")
# getting the indices of key variables
product_idx = headers.index(PRODUCT_ID)    
reordered_idx = headers.index(REORDERED) 
#state_ind = [headers.index(c) for c in job_state if c in headers][0]
# reading the rest of the file
data_list = []
for line in input_file:
    currentline = line.strip('\n').split(",") 
    currentline = [currentline[product_idx], currentline[reordered_idx]]
    data_list.append(currentline)
input_file.close()
# now we write the data to database
create_table1 = '''create table order_products(product_id INTEGER, reordered INTEGER)'''
cur.execute(create_table1)
sql = '''insert into order_products(product_id, reordered) values (%s, %s)'''
for record in data_list:
    try:
        cur.execute(sql, record[0:2])
    except:
        print('error')
        break
    
file2 = 'products.csv'
PRODUCT_ID = 'product_id'
DEPARTMENT_ID = 'department_id'
# reading the file
input_file2 = open(file2, 'r')
headers = input_file2.readline().strip('\n').split(",")
# getting the indices of key variables
product_idx = headers.index(PRODUCT_ID)    
department_idx = headers.index(DEPARTMENT_ID)
# reading the rest of the file
data_list2 = []
for line in input_file2:
    currentline = line.strip('\n').split(",")
    # We will filter only applications which was certified #if currentline[status_ind] == 'CERTIFIED': 
    currentline = [currentline[product_idx], currentline[department_idx]]
    data_list2.append(currentline)
input_file2.close()
# now we write the data to database
create_table2 = '''create table products(product_id INTEGER, department_id INTEGER)'''
cur.execute(create_table2)
sql = '''insert into products(product_id, department_id) values (%s, %s)'''
for record in data_list2:
    try:
        cur.execute(sql, record[0:2])
    except:
        print('error')
        break   

conn.commit()

cur.close()
conn.close()


'''create table test as select a.*, b.department_id from order_products a 
left join products b on a.product_id=b.product_id;'''

'''select department_id, sum(1) as total_order, sum(case when reordered=0 then 1 else 0 end) 
as first_time_order, round(sum(case when reordered=0 then 1.0 else 0 end)/sum(1),2) as ratio 
from test group by department_id order by department_id;
'''

'''
select c.department_id, sum(1) as total_order, sum(case when c.reordered=0 then 1 else 0 end) 
as first_time_order, round(sum(case when c.reordered=0 then 1.0 else 0 end)/sum(1),2) as ratio 
from (select a.*, b.department_id from order_products a 
left join products b on a.product_id=b.product_id) c group by department_id order by department_id;
'''
