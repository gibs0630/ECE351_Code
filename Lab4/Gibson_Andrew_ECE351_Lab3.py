# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 4 #
# Due 14 Feb 2023 #
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
steps = 0.01
steps_0 = -10
steps_f = 10
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly

w_0 = 0.25
h_1 = np.power(np.e,-2*t)*(u(t)-u(t-3))
h_2 = u(t-2)-u(t-6)
h_3 = np.cos(w_0*t)*u(t)

stepresponse = u(t)

plt.figure(0)
plt.plot(t,h_1)
plt.plot(t,h_2)
plt.plot(t,h_3)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 1: Part 1, Functions')
plt.legend(["h_1","h_2","h_3", "u"])


def convolve(f,g):
    y = np.zeros(t.size)
    #offset is in order for zero to work correctly
    for n in range(len(f)):
        for k in range(len(g)):
            if (((n-k) > 0) and ((k-t_offset) > 0) and ((k-t_offset) < len(t))):
                y[n] += f[k-t_offset]*g[n-k]*steps
    return y

h_1cu = convolve(stepresponse,h_1)
h_2cu = convolve(stepresponse,h_2)
h_3cu = convolve(stepresponse,h_3)

plt.figure(1)
plt.plot(t,h_1cu)
plt.plot(t,h_2cu)
plt.plot(t,h_3cu)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 2: Part 2, Convolve with Step Function')
plt.legend(["h_1★u","h_2★u","h_1★u"])


#h_1_int = (-0.5 * np.power(e,-2*t)+0.5)*u(t)-(-0.5*np.power(e,-2*t) -(1)/(-2)*np.power(e,-6))*u(t-3)

h_1_int = 0.5*((1-np.power(np.e,-2*t))*u(t)-(np.power(np.e,-6)-np.power(np.e,-2*t) )*u(t-3))
h_2_int = (t-2)*u(t-2)- (t-6)*u(t-6)
h_3_int = 1/w_0*np.sin(w_0*t)*u(t)

plt.figure(3)
plt.plot(t,h_1_int)
plt.plot(t,h_2_int)
plt.plot(t,h_3_int)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 3: Mathed Out Comparison')
plt.legend(["h_1★u","h_2★u","h_1★u"])

#Questions

#Q1)  Did you work alone or with classmates on this lab? If you collaborated
#   to get to the solution, what did that process look like?
#A1)  I worked alone, but was given the formula for discrete convolution where
#   the time interval is static. I implemented the formula with two for loops,
#   however the return value was incorrect, as I made the error to sum over the
#   wrong iterator ("y[i] += ", when I should have used "y[j] += ").

#Q2)  What was the most difficult part of this lab for you, and what did 
#   your problem-solving process look like?
#A2)  the most difficult part of this lab was understanding the discrete 
#   convolution function.  Once I understood it i could create it via code.
#   However, I also ran into issues where I was trying to use a sum function 
#   to use only one for loop, however that wouldn't have worked as I would have
#   to edit/create new arrays each time it looped.

#Q3)  Did you approach writing the code with analytical or graphical
#   convolution in mind? Why did you chose this approach?
#A3)  My approach was to treat each datapoint as a step function being added, 
#   which would have made things more convusing especially with a plethora 
#   ramps showing up that would have to be resolved.  That method went out the
#   the window once I understood discrete convolution. My final aproach would 
#   best be descrived as analytical.

#Q4)  Leave any feedback on the clarity of lab tasks, expectations, and 
#   deliverables.
#A4)  This lab was strait forward, with the only thing missing was a that had
#   to be solved was knowning what the discrete convolution was and how it 
#   is different from convolution.