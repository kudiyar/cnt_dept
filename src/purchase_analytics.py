# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:16:10 2019

@author: Asus
"""

import sys
# file names
order_products = str(sys.argv[1])
products = str(sys.argv[2])
report = str(sys.argv[3])
# constant variables
PRODUCT_ID = 'product_id'
REORDERED = 'reordered'
DEPARTMENT_ID = 'department_id'
# read the file and sum the orders per product
product_dict = {}
with open(order_products) as file:
    headers = next(file).strip('\n').split(',')
    # indices
    product_id_idx = headers.index(PRODUCT_ID)
    reordered_idx = headers.index(REORDERED)
    for line in file:
        product = line.strip("\n").split(',')[product_id_idx]
        new_order = 0 if int(line.strip("\n").split(',')[reordered_idx]) > 0 else 1
        if product in product_dict:
            product_dict[product][0] += 1
            product_dict[product][1] += new_order
        else:
            product_dict[product] = [1, new_order]
# read the file and sum the products per department
department_dict = {}
with open(products) as file2:
    headers = next(file2).strip('\n').split(',')
    product_id_idx = headers.index(PRODUCT_ID)
    department_id_idx = -1  # it is the last column
    for line in file2:
        department = int(line.strip("\n").split(',')[department_id_idx])
        product =  line.strip("\n").split(',')[product_id_idx]
        if department in department_dict:
            try:
                department_dict[department][0] += product_dict[product][0]
                department_dict[department][1] += product_dict[product][1]
            except KeyError:
                continue
        else:
            try:
                department_dict[department] = [product_dict[product][0], product_dict[product][1]]
            except KeyError:
                continue
 # sort the dictionary based on department in ascending order           
sorted_departments = sorted(department_dict.items(), key=lambda x: x[0])
# write to a file
with open(report,"w") as report_file:
    report_file.write("department_id,number_of_orders,number_of_first_orders,percentage\n")
    for tupl in sorted_departments:
        report_file.write('{}, {}, {}, {}'.format(tupl[0], tupl[1][0], 
                              tupl[1][1], round(tupl[1][1]/tupl[1][0], 2)))
        report_file.write('\n')


