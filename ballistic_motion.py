#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:14:13 2018

@author: mitchellyoung
"""
import math as ma
import matplotlib
import matplotlib.pyplot as plot

#inputs
yi=float(raw_input("Initial Height [m]: "))
vi=float(raw_input("Initial Velocity [m/s]: "))
theta=float(raw_input("Angle [°]: "))
a=float(raw_input("Acceleration [m/s^2](Be careful of direction): "))
timestep=float(raw_input("Timestep [s]: "))


#math mods
vx=vi*ma.cos(theta*ma.pi/180)
viy=vi*ma.sin(theta*ma.pi/180)

vy_now=viy
y_now=yi
x_now=0
t=0

#lists
    #y=height x=distance, v=velocity, a=acceleration, i=initial, f=final
time_list=[]
x_list=[]
y_list=[]
vy_list=[]

while y_now>=0: 
    time_list.append(round(t*timestep,5))
    vy_list.append(round(vy_now,5))
    y_list.append(round(y_now,5))
    y_now=y_now+vy_now*timestep
    vy_now=vy_now+a*timestep
    x_list.append(round(x_now,5))
    x_now=x_now+vx*timestep
    t=t+1


plot.plot(x_list,y_list)

#from https://matplotlib.org/examples/pylab_examples/equal_aspect_ratio.html
plot.xlabel("Distance (m)")
plot.ylabel("Height (m)")
plot.title("Ballistic Motion")
plot.grid(True)
plot.axes().set_aspect("equal", "datalim")

plot.show()
