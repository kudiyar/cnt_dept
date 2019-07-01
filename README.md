# Purchase-Analytics

## Table of Contents
1. [Problem](README.md#problem)
1. [Solution](README.md#solution)
1. [Technical part](README.md#technical_part)
1. [Notes](README.md#notes)

## Problem

Instacart published a sales data on different products. I need to find the total sales per department outlining first time orders and its ratio to total sales. 

## Solution

We are given two csv format type files. There is sales order data based on a product in `order_products.csv` file. From this file, I extract total number of sales per product and respective first time order count. In the `products.csv` file, products are categorized by departments. Since I have total number of sales per product from the first file, I sum total number of sales of all products belonging to the same department.  

## Technical part

I used dictionaries for faster lookup where I had products and departments as keys. The list containing total number of sales and first time number of sales was the value for the key. The list is updated by summing the elements per product and per department respectively. 

## Notes

* The repository was organized as per guidelines
* The code contains sixty lines so did not make modular as I did not see any need for it
* The repository is private but will be made public after the deadline


**Thanks for reading and reviewing my work**
