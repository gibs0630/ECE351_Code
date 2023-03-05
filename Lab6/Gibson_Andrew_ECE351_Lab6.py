# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 6 #
# Due 28 Feb 2023 #
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


steps = 0.01
steps_0 = 0
steps_f = 2
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly


y_hand = np.exp(-6*t)*u(t)-1/2*np.exp(-4*t)*u(t)+1/2*u(t)

t_sig, y_sig = sig.step(([1,6,12],[1,10,24]),  T = t)


plt.figure(0)
plt.plot(t,y_hand, linewidth = "6")
plt.plot(t,y_sig, linewidth = "3")
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 1: Part 1, Step Response')
plt.legend(["hand calculation", "scipy.signal.step"])



# residue format
#sum from i = 0 to n [R_i/(s+P_i)+K_i]

print("transfer function")
R, P, K = sig.residue([1,6,12],[1,10,24])

print("R", R)
print("P", P)
print("K", K)

#R [ 2. -6.]
#P [-4. -6.]
#K [1.]
#
#H(s) = -6/(s+6) + 2/(s+4) + 1


print("")
print("step response")
R, P, K = sig.residue([1,6,12],[1,10,24,0])

print("R", R)
print("P", P)
print("K", K)


#R [ 0.5 -0.5  1. ]
#P [ 0. -4. -6.]
#K []
#
#Y(s) = 1/(s+6)-0.5/(s+4)+0.5/s




# Part 2


steps = 0.01
steps_0 = 0
steps_f = 4.5
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly


print("")
print("system")

R, P, K = sig.residue([25250],[1, 18, 218, 2036, 9085, 25250])

print("R", R)
print("P", P)
print("K", K)

def cosine_method_from_Y_of_s(t, R, P, K):
    y=np.zeros(t.shape)
    
    
    for i in range(len(t)):
        if (t[i] > 0):
            for k in range(len(R)):
                y[i] +=  np.abs(np.real(R[k]))*np.exp(np.real(P[k])*t[i])*np.cos(np.imag(P[k])*t[i]+np.angle(R[k],deg=False))
            for k in range(len(K)):
                y[i] +=  K[k]
        else:
            y[i] = 0
        
    return y


y_cos = cosine_method_from_Y_of_s(t, R, P, K)
t_cos_step, y_cos_step = sig.step(([25250],[1, 18, 218, 2036, 9085, 25250]),T=t)

plt.figure(1)
plt.plot(t,y_cos)
plt.plot(t,y_cos_step)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 4: Part 2, Difficult System')
plt.legend(["cosine method (transfer function)", "scipy.signal.step (step response)"])


# Questions

#Q1) For a non-complex pole-residue term, you can still use the cosine method, 
# explain why this works.
#A1) You can still use the cosine method because when both the numerator and
# denominator of the terms, "a / (s+b)", are in the real domain, then
# the angular frequency and angular displacement are 0. cosine of 0 is 1, which
# then harmlessly removes the term and we end up with out when the expected 
# "a*e^{-bt}" equation

#Q2) Leave any feedback on the clarity of the expectations, instructions, and 
# deliverables.
#A2) The provided book does not list a complete exhaustive list of identities
# that can be used to derive laplaces and their inverses, however there was a
# clear confusion in the idenitying what term is laplaced in the "The Cosine 
# Method" section of the book as compared to the 4.3 task 3 of the lab.  If
# there was a formula written out for accepting complex roots in isolation 
# compared to when paired up with their complement, it woudl be easier to
# understand.

