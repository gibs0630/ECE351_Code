# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 2 #
# Due 31 Jan 2023 #
# User-Defined Functions #
# https://github.com/gibs0630/ECE351\_Code #
# https://github.com/gibs0630/ECE351\_Reports #
# #
################################################################
import numpy as np
import matplotlib.pyplot as plt

#Part 1
def func1(t):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        y[i] = np.cos(t[i])
    return y

steps = 1
t = np.arange(0,10,steps)
y = func1(t)

plt.figure(0)
plt.plot(t,y)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 1: Part 1, func1')

#Part 2

#y(t) = r(t)-r(t-3)+5u(t-3)-2u(t-6)-2r(t-6)
def u(t):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        if (t[i] > 0):
            y[i] = 1
        else:
            y[i] = 0
    return y

def r(t):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        if (t[i] > 0):
            y[i] = t[i]
        else:
            y[i] = 0
    return y

t2 = np.arange(-5,10,steps)
yr = r(t2)
yu = u(t2)

plt.figure(2)
plt.grid()
plt.plot(t2,yr)
plt.plot(t2,yu)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 2: Demonstration of Step and Ramp Functions')

def func2(t):
    return r(t)-r(t-3)+5*u(t-3)-2*u(t-6)-2*r(t-6)

y2 = func2(t2)

plt.figure(3)
plt.grid()
plt.plot(t2,y2)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 3: Part 2, func2')


#Part 3
#def rev(t):
#    y = np.zeros(t.shape)
    
 #   for i in range(len(t)):
#        y[i] = 0-t[i]
#    return y

t3 = np.arange(-15,15,steps)

y3 = func2(0-t3)

plt.figure(4)
plt.grid()
plt.plot(t3,y3)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 4: Time Reversed')


y4 = func2(t3-4)
y5 = func2(-t3-4)

plt.figure(5)
plt.grid()
plt.plot(t3,y4)
plt.plot(t3,y5)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 5: Time Shift')


y6 = func2(0.5*t3)
y7 = func2(2*t3)

plt.figure(6)
plt.grid()
plt.plot(t3,y6)
plt.plot(t3,y7)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 6: Time Scale')


y8 = np.diff(func2(t2)) / np.diff(t2)

plt.figure(7)
plt.grid()
plt.plot(t2,y2)
plt.plot(t2[0:t2.size-1],y8)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 9: Derivative of func2')
plt.ylim(-3,9)


#Questions

#Q1)  Are the plots from Part 3 Task 4 and Part 3 Task 5 identical?
#   is it possible for them to match? Explain why or why not.
#A1)  The hand drawn plot is a representation of mathamatics while
#   the python plot is a representation of datapoints. They appear 
#   close but are not identical

#Q2)  How does the correlation between the two plots (Part 3 Task 4 
#   and Part 3 Task 5 ) change if you were to change the step size
#   within the time variable in task 5? Explain why this happens.
#A2)  When the interval between datapoints increases, the more jagged
#   and less information is presented, this will cause eratic change
#   as the noise that would be information cannot be parsed from the
#   large timegaps.  This will make the two graphs to become less
#   nearly identical to clearly different as the interval increases.

#Q3)  Leave any feedback on the clarity of lab tasks, expectations, 
#   and deliverables
#A3)  The format of the lab instructions was at first confusing 
#   because there was a bit of douplication ("2.Deliverables 
#   Overview", "Deliverables" in each section, and in the tasks 
#   themselves.