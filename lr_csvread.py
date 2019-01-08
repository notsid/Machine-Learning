#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:04:27 2019

@author: sidgan22
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Linear Regression with simple data fed as an array
def plotline(x,y,x1,y1):
    plt.scatter(x,y,color='b',s=10)
    plt.plot(x,y1,color='g' ,linewidth=2)
    plt.axis([0,80,0,200])
    plt.xlabel('Temperature(Farenheit)')
    plt.ylabel('Bikes Rented(Units)')
    plt.title('Bike Rental(Linear Regresion)')
    plt.show()
    
def run():
    #data input
    md=pd.read_csv('/home/sidgan22/Desktop/Code/ML/data.csv')    
    x=md.iloc[:,0].values
    y=md.iloc[:,1].values
    
    #Coefficients compute 
    mx=x.mean()
    my=y.mean()
    
    #k=x-x(mean)
    k=x-mx
    
    #m0 is slope of predicted line
    m0=np.sum(k.dot((y-my)))/np.sum(k**2)
    
    #c0 is the coefficient in the equation of a straight line
    c0=my-(m0*mx)
    print(m0,c0)
    #yg is the equation of predicted line
    #yg=m0*x+c0
  
    #Line plot
    x1=[25,71]
    y1=m0*x+c0
    plotline(x,y,x1,y1)
    
if __name__ == "__main__":
    run()