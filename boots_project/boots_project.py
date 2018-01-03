#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:26:31 2017

@author: gioia


"""
import random
import matplotlib.pyplot
import bootsframework
import csv

#create stores that are set in a location 

stores=[]
customers = []
distances =[]
revenue_list = []
final_revenue_list=[]


num_of_stores = 8
num_of_customers = 50
num_of_iterations= 100
money = 100

#read data: this file contains the revenues of the stores. 

file = open("revenue.csv", "r")
reader = csv.reader(file)

#create a list of revenues 
#the revenues are appended by default as strings. the following code turns the strings into integers
for i in reader:
    i = str(i)
    i= i.strip("'[]'")
    revenue_list.append(int(i))

#We can print the revenue list to make sure that they are integers
#print(revenue_list)

#create stores
for i in range(num_of_stores):
    stores.append(bootsframework.Store((i+1), revenue_list[i]))
#assign store numbers (1-8) to stores)

#generate customers 
for i in range (num_of_customers):
    customers.append(bootsframework.Customer(customers,stores,money))
#print (customers)

#make customer move and shop randomly without wandering off the plane
for j in range(num_of_iterations):
    random.shuffle(customers)
    for i in range(num_of_customers):
        customers[i].move()
        customers[i].shop()

#this for loop updates the revenue of the stores in the store list using the revenues from the customers store list        
for i in range(num_of_stores):
    for j in range(num_of_customers):
        stores[i].revenue = (stores[i].revenue + customers[j].stores[i].revenue)

#append the new revenues to the new list
for i in range(num_of_stores):
    final_revenue_list.append(stores[i].revenue)

#check the updated revenue list before writing it to the file
print (revenue_list)
print(final_revenue_list)
               
#write a file that will show the final revenue of each store. 
finalrevenue= open("finalrevenue.csv", "a")
writer = csv.writer(finalrevenue) 

for i in final_revenue_list:
    i = str(i)
    writer.writerow(i)
    
finalrevenue.close
       
#plot the graph
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_stores):
    matplotlib.pyplot.scatter(stores[i].x ,stores[i].y, color='blue')
for i in range (num_of_customers):
    matplotlib.pyplot.scatter(customers[i].x ,customers[i].y, color='tan')
# colour the the customer closest to a shop a different colour
matplotlib.pyplot.show()

file.close