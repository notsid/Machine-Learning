#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:44:28 2019

@author: sidgan22
"""
import numpy as np
import matplotlib.pyplot as plt
#Linear Regression with simple data fed as an array
def plotline(x,y,x1,y1):
    plt.scatter(x,y,color='b',s=10)
    plt.plot(x1,y1,color='g' ,linewidth=2)
    plt.axis([-1,9,1,12])
    plt.xlabel('Age (Years)')
    plt.ylabel('Weight (kg)')
    plt.title('Linear Regression(OLS)')
    plt.show()
    
def run():
    #data input
    a=[]
    for i in range(0,7):
        a.append(i)
        a.append(i+0.5)
    b=[3.5,4.2,3.95,4.25,4.6,4.67,5.3,5.8,6.4,6.9,7.6,8.1,8.5,9.22]
        
    x=np.array(a)
    y=np.array(b)
    
    #Coefficients compute 
    mx=x.mean()
    my=y.mean()
    
    #k=x-x(mean)
    k=x-mx
    
    #m0 is slope of predicted line
    m0=np.sum(k.dot((y-my)))/np.sum(k**2)
    
    #c0 is the coefficient in the equation of a straight line
    c0=my-(m0*mx)
    
    #yg is the equation of predicted line
    #yg=m0*x+c0
  
    #Line plot
    x1=[0,(len(x)-1)/2]
    y1=[c0+m0*x[0],c0+m0*x[len(x)-1]]
    plotline(x,y,x1,y1)
    
if __name__ == "__main__":
    run()