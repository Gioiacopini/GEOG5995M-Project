#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:16:25 2017

@author: gioia
"""

import random 

#use capital letter for name of the class because of PascalCasing

class Store: #store class has 2 variables "store_number" and "revenue"
    def __init__ (self, store_number, revenue):#init is the initalizer of the class
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.store_number = store_number
        self.revenue = revenue
        
        
        
#create a customer class     
class Customer:
    def __init__ (self, customers, stores, money):
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.customers = customers
        self.stores = stores
        self.money = money

    
    def move (self):
        if random.random()< 0.5:
            self.x = (self.x + 1) %99
        else:
            self.x = (self.x - 1) %99        
        
        if random.random()< 0.5:
             self.y = (self.y + 1) %99
        else:
             self.y = (self.y - 1) %99

#calculate the distance between the customers and the stores in steps   
    def distance_from_store(self, store):
        store_distance = abs(self.x - store.x) + abs(self.y - store.y)
        return store_distance
    
    def check_closest_store (self):
        for store in self.stores:
            closeness = self.distance_from_store(store)
            if closeness<=2:
              #print ("closest store =" + str(store.store_number))
              return store.store_number
            #if every store is more than 5 steps away the function retuns 0 
        #print ("far from every store")
        return 0
    
    def shop (self):
        closest_store_number = self.check_closest_store()
        if (closest_store_number > 0):
            if (self.money >= 10):
                self.money -= 10
                print ("Shopping at store " + str(closest_store_number))
                self.stores[closest_store_number - 1].revenue += 10 
            #print ("Broke Customer")
        
                    

        
