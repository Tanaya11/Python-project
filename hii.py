# -*- coding: utf-8 -*-
"""
Created on Sun May 01 23:22:44 2016

@author: aditya
"""
import math
import scipy
import numpy.random as npr
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import statsmodels.stats.stattools as stools


t=scipy.array([0,45, 60, 70, 80, 90 ,100 ,120])
yexpt=scipy.array([40,30,25,20,15,10,5,2])

def function(t,a,b,c,d):
    ymodel=a*t*t*t+b*t*t+c*t+d
    return ymodel
    
def residuals(p,yt,t):
    a,b,c,d=p
    
    m=yt-function(t,a,b,c,d)
    return m
p0=[0,0,0,0]


soln1=leastsq(residuals,p0,args=(yexpt,t))
print soln1[0]
    
       

    
    