#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:26:31 2017

@author: gioia


"""
import random
import matplotlib.pyplot
import bootsframework

#create stores that are set in a location 

stores=[]
customers = []
distances =[]

num_of_stores = 8
num_of_customers = 50
num_of_iterations= 500
revenue = 0
money = 100

#create stores
for i in range(num_of_stores):
    stores.append(bootsframework.Store((i+1), revenue))
#assign stone sumbers (1-8) to stores)

#generate customers 
for i in range (num_of_customers):
    customers.append(bootsframework.Customer(customers,stores,money))
#print (customers)

#make customer move and shop randomly without wandering off the plane
for j in range(num_of_iterations):
    random.shuffle(customers)
    for i in range(num_of_customers):
        customers[i].move()
        #customers[i].check_closest_store()
        customers[i].shop()

#make function that will update the revenue of the stores in the store list using the revenues from the customers store list
#write a file that will show the revenue of each store. 
        
#plot the graph
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_stores):
    matplotlib.pyplot.scatter(stores[i].x ,stores[i].y, color='blue')
for i in range (num_of_customers):
    matplotlib.pyplot.scatter(customers[i].x ,customers[i].y, color='tan')
# colour the the customer closest to a shop a different colour
matplotlib.pyplot.show()
