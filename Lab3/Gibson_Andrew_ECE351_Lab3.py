# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 3 #
# Due 7 Feb 2023 #
# User-Defined Functions #
# https://github.com/gibs0630/ECE351\_Code #
# https://github.com/gibs0630/ECE351\_Reports #
# #
################################################################
import numpy as np
import matplotlib.pyplot as plt


#functions
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

#Part 1
steps = 0.001
t = np.arange(0,20,steps)

f_1 = u(t-2)-u(t-9)
f_2 = np.power(np.e,-t)*u(t)
f_3 = r(t-2)*(u(t-2)-u(t-3))+r(4-t)*(u(t-3)*u(t-4))

plt.figure(0)
plt.plot(t,f_1)
plt.plot(t,f_2)
plt.plot(t,f_3)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 1: Part 1, Ramps and Steps')
plt.legend(["f_1","f_2","f_3"])


def convolve(f,g):
    y=np.zeros(t.shape)
    
    
    for i in range(len(t)):
        for j in range(len(t)):
            if ((j-i) < 0):
                continue
            else:
                y[j] += f[i]*g[j-i]
    return y

f_1cf_2 = convolve(f_1,f_2)
f_2cf_3 = convolve(f_2,f_3)
f_1cf_3 = convolve(f_1,f_3)

plt.figure(1)
plt.plot(t,f_1cf_2)
plt.plot(t,f_2cf_3)
plt.plot(t,f_1cf_3)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 2: Part 2, Convulsions')
plt.legend(["f_1★f_2","f_2★f_3","f_1★f_3"])


f_1cf_2_numbly = np.convolve(f_1,f_2)
f_2cf_3_numbly = np.convolve(f_2,f_3)
f_1cf_3_numbly = np.convolve(f_1,f_3)

plt.figure(2)
plt.plot(t,f_1cf_2_numbly[0:t.size])
plt.plot(t,f_2cf_3_numbly[0:t.size])
plt.plot(t,f_1cf_3_numbly[0:t.size])
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 3: Part 2, Convulsions using numpy.convulve')
plt.legend(["f_1★f_2","f_2★f_3","f_1★f_3"])


plt.figure(3)
plt.plot(t,f_1cf_2_numbly[0:t.size]-f_1cf_2)
plt.plot(t,f_2cf_3_numbly[0:t.size]-f_2cf_3)
plt.plot(t,f_1cf_3_numbly[0:t.size]-f_1cf_3)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 4: Part 2, Method Error')
plt.legend(["f_1★f_2","f_2★f_3","f_1★f_3"])

#Questions

#Q1)  Did you work alone or with classmates on this lab? If you collaborated
#   to get to the solution, what did that process look like?
#A1)  I worked alone, but was given the formula for descrete convolution where
#   the time interval is static. I implemented the formula with two for loops,
#   however the return value was incorrect, as I made the error to sum over the
#   wrong itterator ("y[i] += ", when I should have used "y[j] += ").

#Q2)  What was the most difficult part of this lab for you, and what did 
#   your problem-solving process look like?
#A2)  the most difficult part of this lab was understanding the descrete 
#   convolution function.  Once I understood it i could create it via code.
#   However, I also ran into issues where I was trying to use a sum function 
#   to use only one for loop, however that wouldn't have worked as I would have
#   to edit/create new arrays each time it looped.

#Q3)  Did you approach writing the code with analytical or graphical
#   convolution in mind? Why did you chose this approach?
#A3)  My approach was to treat each datapoint as a step function being added, 
#   which would have made things more convusing especially with a plethora 
#   ramps showing up that would have to be resolved.  That method went out the
#   the window once I understood descrete convolution. My final aproach would 
#   best be descrived as analytical.

#Q4)  Leave any feedback on the clarity of lab tasks, expectations, and 
#   deliverables.
#A4)  This lab was strait forward, with the only thing missing was a that had
#   to be solved was knowning what the discrete convolution was and how it 
#   is different from convolution.