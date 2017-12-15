#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:16:25 2017

@author: gioia
"""

import random 

#use capital letter for name of the class because of PascalCasing

class Stores:
    def __init__ (self, stores):#init is the initalizer of the class
        self.x = (95,12,67,64,54,47,53,29)
        self.y = (30,51,80,9,9,51,36,95)
        self.stores = stores
        self.revenue = 0
        
        
class Customers:
    def __init__ (self, customers):
        self.x = (random.randint(0,100))
        self.y = (random.randint(0,100))
        self.customers = customers
        #self.stores = stores
        self.money = 100
    
    def move (self):
        if random.random()< 0.5:
            self.x = (self.x + 1) %99
        else:
            self.x = (self.x - 1) %99        
        
        if random.random()< 0.5:
             self.y = (self.y + 1) %99
        else:
             self.y = (self.y - 1) %99
    
    def distance_from_store(self, stores):
        return(((self.x - stores.x)**2)+ ((self.y - stores.y)**2)**0.5)

    def shop (self, stores):
        for customers in self.customers:
            for stores in self.stores:
                dist = self.distance_from_store(stores)
                if dist <= 0.5:
                    self.money = (self.money - 10)
                    self.revenue = (self.money + 10)
            
            
            
        
             

    
#for customer0 in customers:
    #for store0 in stores:
        #distance = distance_from_store(customer0, store0)
        #distances.append([distance])
        #print(distances)
    