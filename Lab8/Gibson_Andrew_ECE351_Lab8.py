# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 8 #
# Due 21 Mar 2023 #
# User-Defined Functions #
# https://github.com/gibs0630/ECE351\_Code #
# https://github.com/gibs0630/ECE351\_Reports #
# #
################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

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


steps = 0.1
steps_0 = 0
steps_f = 20
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly



#====part1====

#----task1----
T = 8
w_0  = 2*np.pi/T

a_0 = 0

a_k = 0

def b_k(k): 
    return 2/(k*np.pi)*(1-np.power(-1,k))


print ("a_0", a_0)

a_1 = a_k
print ("a_1", a_1)

b_1 = b_k(1)
print ("b_1", b_1)

b_2 = b_k(2)
print ("b_2", b_2)

b_3 = b_k(3)
print ("b_3", b_3)


#----task2----
def fourier_square(t,N):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        k = 1
        
        y[i] = a_0
        
        while k <= N:
            y[i] += np.cos(k*w_0*i*steps) * a_k   +np.sin(k*w_0*i*steps) *b_k(k)
            k += 1
        
        
    return y

f_1 = fourier_square(t,1)
f_3 = fourier_square(t,3)
f_15 = fourier_square(t,15)
f_15 = fourier_square(t,15)
f_50 = fourier_square(t,50)
f_150 = fourier_square(t,150)
f_1500 = fourier_square(t,1500)

plt.figure(0)

plt.plot(t, f_1)
plt.plot(t, f_3)
plt.plot(t, f_15)

plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 2: Fourier Series with small N')
plt.legend(["N=1","N=3","N=15"])



plt.figure(1)

plt.plot(t, f_50)
plt.plot(t, f_150)
plt.plot(t, f_1500)

plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 3: Fourier Series with Large N')
plt.legend(["N=50","N=150","N=1500"])

plt.figure(2)

#title page image
#f_10000 = fourier_square(t,10000)
#plt.plot(t, f_10000)

#plt.xlabel('t [s]')
#plt.ylabel('y(t)')


# Questions
#Q1) Is x(t) an even or an odd function? Explain why. 
#A1) x(t) is an odd function, because if you multiplied t by -1 and then 
# multiplied the output by -1, you would get the original function.

#Q2) Based on your results from Task 1, what do you expect the values of a_2, 
# a_3, . . . , a_n to be? Why?
#A2) a_k should be 0, because when solving for it, there were no other terms 
# beside 0.

#Q3) How does the approximation of the square wave change as the value of N 
# increases? In what way does the Fourier series struggle to approximate the 
# square wave?
#A3) As the value of N increases, the wave becomes more and more square like 
# and the plateauss and valleys become more and more flat. The Fourier series 
# does struggle to get approximations at the impulse moments when it 
# transitions from 1 to -1 and from -1 to 1.

#Q4) What is occurring mathematically in the Fourier series summation as the 
# value of N increases?
#A4) As N increases, a more sine waves are being added to the output.

#Q5) Leave any feedback on the clarity of lab tasks, expectations, and 
# deliverables.
#A5) For the periodic function used in this lab, a_0 and a_k were 0, this 
# caused confusion as the function a_k for this case would always output 0.
# I would think # that this lab would be better, or at least more clear on the 
# what you are suppose to do on part 1 task 2, if we were to program the code
# that would take any function with a period (sequence of datapoints that would
# repeat outside of it's range), then the lab could have us "use" python to 
# solve for a_0 and a_0 for any function period.
# Also, the equations in the lab handout sheet do not distinguish between x_0 
# and x, where x$_0$ is the period of the function output of the period range.



