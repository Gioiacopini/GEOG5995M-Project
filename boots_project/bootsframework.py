#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:16:25 2017

@author: gioia
"""

import random 

#use capital letter for name of the class because of PascalCasing

class Store:
    def __init__ (self, stores, revenue):#init is the initalizer of the class
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        self.stores = stores
        self.revenue = revenue
        
        
        
        
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
    
    def check_closest_store (self, store):
        for customer in self.customers:
            for store in self.stores:
                closeness = self.distance_from_store(store)
                if closeness<=5:
                    print ("closest store =" + self.store
                
                    

        
