# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 11 #
# Due 11 Apr 2023 #
# User-Defined Functions #
# https://github.com/gibs0630/ECE351\_Code #
# https://github.com/gibs0630/ECE351\_Reports #
# #
################################################################
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy as scipy

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

def cos(t, f = 1/(2*np.pi), offset = 0):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        y[i] = np.cos(2*np.pi*f*(i*steps-steps_0-offset))
    return y

def sin(t, f = 1/(2*np.pi), offset = 0):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        y[i] = np.sin(2*np.pi*f*(i*steps-steps_0-offset))
    return y

steps = 0.00002/8
steps_0 = 0
steps_f = 0.01
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly

s_steps = 100
s_steps_0 = 1e3
s_steps_f = 1e6
s = np.arange(s_steps_0,s_steps_f,s_steps)

#====part1====

#---task 1---
# y[k] = 2 x[k] - 40 x[k-1] + 10 y[k-1] - 16 y[k-2]

# y[k] is causal, so both the left hand side and right hand side are multiplied by u[k]

# Y[z] = 2 X[z] - 40 (z^-1 X[k] + x[-1]) + 10 (z^-1 Y[k] + y[-1])-16 (z^-2 Y[k] + z^-1 y[-1]+ y[-2])

# Y[z] = 2 X[z] - 40 (z^-1 X[k] + (0)) + 10 (z^-1 Y[k] + (0)) - 16 (z^-2 Y[k] + z^-1 (0) + (0))

# Y[z] = 2 X[z] - 40(z^-1 X[k] + 10 z^-1 Y[k] - 16 z^-2 Y[k]

# 16 z^-2 Y[k] - 10 z^-1 Y[k] + Y[z] = 2 X[z] - 40 z^-1 X[k]

# (16 z^-2 - 10 z^-1 + 1) Y[z] = (2 - 40 z^-1) X[k]

# (Y[z]) / (X[k]) = (2 - 40 z^-1) / (16 z^-2 - 10 z^-1 + 1)

# H[k] = (2 - 40 z^-1) / (16 z^-2 - 10 z^-1 + 1)

# H[k] = (2 z^2 - 40 z^1) / (16 - 10 z^1 + 1z^2)

# H[k]/z = (2 z - 40) / (16 - 10 z^1 + 1z^2)

# H[k]/z = (2 z - 40) / (z^2 - 10 z^1 + 16)

# H[k] = (2 z^2 - 40z) / (z^2 - 10 z^1 + 16)


#---task 2---

# H[k]/z = (2 z - 40) / (z^2 - 10 z^1 + 16)

# (2 z - 40) / ((z-8)(z-2)) = A / (z-8) + B / (z-2)

# A = (2 z - 40) / (z-2) | z = 8

# A = -4

# B = (2 z - 40) / (z-8) | z = 2

# B = 6


# H[k]/z = -4 / (z-8) + 6 / (z-2)

# H[k] = (-4 z) / (z-8) + (6 z) / (z-2)

# H[k] = (-4 z) / (z-8) + (6 z) / (z-2)


# h[k] = (-4) 8^k u[k]+ (6) 2^k u[k]


#---task 3---

r1, p1, k1 = scipy.signal.residuez([2,-40],[1,-10,16])

print ("")
print ("task 3")
print ("r: ", r1, ", p: ", p1, ", k: ", k1)

# task 3
# r:  [ 6. -4.] , p:  [2. 8.] , k:  []


#---task 4---

#
# Copyright ( c ) 2011 Christopher Felton
#
# This program is free software : you can redistribute it and / or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation , either version 3 of the License , or
# ( at your option ) any later version .
#
# This program is distributed in the hope that it will be useful ,
# but WITHOUT ANY WARRANTY ; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE . See the
# GNU Lesser General Public License for more details .
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program . If not , see < http :// www . gnu . org / license s / >.
#
# The following is derived from the slides presented by
# Alexander Kain for CS506 /606 " Special Topics : Speech Signal Processing "
# CSLU / OHSU , Spring Term 2011.
#
#
#
# Modified by Drew Owens in Fall 2018 for use in the University of Idaho ’s
# Department of Electrical and Computer Engineering Signals and Systems I Lab
# ( ECE 351)
#
# Modified by Morteza Soltani in Spring 2019 for use in the ECE 351 of the U of
# I .
#
# Modified by Phillip Hagen in Fall 2019 for use in the University of Idaho ’s
# Department of Electrical and Computer Engineering Signals and Systems I Lab
# ( ECE 351)

def zplane (b , a , filename = None ) :
    """ Plot the complex z - plane given a transfer function """

    import numpy as np
    import matplotlib . pyplot as plt
    from matplotlib import patches
    
    # get a figure / plot
    ax = plt . subplot (1 , 1 , 1)
    
    # create the unit circle
    uc = patches . Circle ((0 ,0) , radius =1 , fill = False , color = 'black' , ls = 'dashed')
    ax . add_patch ( uc )
    
    # the coefficients are less than 1 , normalize the coefficients
    if np . max ( b ) > 1:
        kn = np . max ( b )
        b = np . array ( b ) / float ( kn )
    else :
        kn = 1
    
    if np . max ( a ) > 1:
        kd = np . max ( a )
        a = np . array ( a ) / float ( kd )
    else :
        kd = 1
        
    # get the poles and zeros
    p = np . roots ( a )
    z = np . roots ( b )
    k = kn / float ( kd )
    
    # plot the zeros and set marker properties
    t1 = plt . plot ( z . real , z . imag , 'o' , ms =10 , label =  'Zeros')
    plt . setp ( t1 , markersize =10.0 , markeredgewidth =1.0)
    
    # plot the poles and set marker properties
    t2 = plt . plot ( p . real , p . imag , 'x' , ms =10 , label = 'Poles')
    plt . setp ( t2 , markersize =12.0 , markeredgewidth =3.0)
    plt.title('Figure 2: zplane')# my code so that it gets a title
    
    ax . spines [ 'left' ]. set_position ( 'center')
    ax . spines [ 'bottom' ]. set_position ( 'center')
    ax . spines [ 'right' ]. set_visible ( False )
    ax . spines [ 'top' ]. set_visible ( False )
    
    plt . legend ()
    
    # set the ticks
    
    # r = 1.5; plt . axis ( ’ scaled ’) ; plt . axis ([ -r , r , -r , r ])
    # ticks = [ -1 , -.5 , .5 , 1]; plt . xticks ( ticks ) ; plt . yticks ( ticks )
    
    if filename is None :
        plt . show ()
    else :
        plt . savefig ( filename )
    
    return z , p , k

zplane([2,-40],[1,-10,16])



#---task 5---

plt.figure(2)
w3, h3 = scipy.signal.freqz([2,-40],[1,-10,16], whole = True)

plt.figure(2)
plt.plot(w3,h3)
plt.ylabel('gain')
plt.xlabel('w(rad/s)')
plt.title('Figure 3: freqz')




# Questions
#Q1) Looking at the plot generated in Task 4, is H(z) stable? Explain why or why not.
#A1) zeroes have no effect on stability, so we can ignore the zero at 20
# Sue to the relation 𝓩{a^k u[k]} = z / (z-a), then if a is is less then one, then it is stable. looking at the plot, there are two poles, and both are outside the unit circle, thus this . This would be causal function would be unstable.

#Q2) Leave any feedback on the clarity of lab tasks, expectations, and deliverables
#A2) the poles and zeroes plot was new, perhaps an explanation of what it is prior to the lab would be helpful for future classes.
