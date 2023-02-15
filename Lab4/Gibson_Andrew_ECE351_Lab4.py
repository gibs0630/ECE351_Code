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

#Q1) Leave any feedback on the clarity of lab tasks, expectations, and 
#   deliverables.
#A1) Because my convolution assumed that the index started at zero, I had to 
#   rewrite my function entirely in order to accommodate that. while I was
#   fixing that I also corrected for the change in amplitude based on the step 
#   size.