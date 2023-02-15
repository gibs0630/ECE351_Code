# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 5 #
# Due 21 Feb 2023 #
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


steps = 0.00000001
steps_0 = 0
steps_f = 0.0012
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly

#Part 1
R = 1000
L = 0.027
C = 100E-9

w_0 = np.sqrt(1/(C*L)-np.power(1/(2*R*C),2))
a_0 = 1/(2*R*C)
h_0 = np.power(np.e,(-a_0*t))*(2*a_0*np.cos(w_0*t)-(2*a_0*a_0)/w_0*np.sin(w_0*t))*u(t)

w_1 = (1/2)*np.sqrt(np.abs(np.power(1/(R*C),2)-4*(1/(L*C))))
a_1 = -1/(2*R*C)
g_m = np.sqrt(np.power(w_1/(R*C),2)+np.power(a_1/(R*C),2))
g_a = np.arctan2(w_1/(R*C),a_1/(R*C))
h_1 = np.abs(g_m)/w_1*np.power(np.e,a_1*t)*np.sin(w_1*t+g_a)*u(t)

num = [0,1/(R*C),0]
den = [1,1/(R*C),1/(C*L)]

tout, yout = sig.impulse ((num, den), T=t)

plt.figure(0)
plt.plot(t,h_0, linewidth = 9, color = "red")
plt.plot(t,h_1, linewidth = 6, color = "yellow")
plt.plot(tout,yout, linewidth = 2,color = "green")
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 1: Part 1, Impulse Response')
plt.legend(["hand calulaction","sine method", "sig.impulse"])

#Part 2



tout2, yout2 = sig.step ((num, den), T=t)

# stepresponse = u(t)

plt.figure(1)
plt.plot(tout2,yout2)
plt.plot(tout,yout/20000)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 2: Part 2, Comparison with impulse and step.')
plt.legend(["sig.step","sig.impulse/20000"])



#lim from s -> 0 [s*H(s)] = lim from t -> inf [f(t)]

#do the poles prevent an existance? there are no real poles

#lim from s -> 0 [s*H(s)] = 
#lim from s -> 0 [s*(s/(R*C) / (s^2+s/(R*C)+1/(C*L)))] = 
#lim from s -> 0 [((R*C) / (1+(R*C)/s+1/(C*L*s^2)))] = 
#0*(0/(R*C) / (0^2+0/(R*C)+1/(C*L))) = 
#0

#thus 
#lim from t -> inf [f(t)] = 0



#The impulse response momentary jitters the circuit until it will resettle
# where the resistor will absorb the back and forth motion, diminishing the
# voltage until it reaches 0. The step function also will have the voltage
# diminish to zero as the inductor will slowly begin to act like an open
# circuit.
#Also, the reason the impulse is 20000 times larger is because of the nature of
# the impulse (spontaneously large amount of voltage over a small time 
# interval)where as the step is way smaller.both of they decaying at the same
# time makes sense as well as when taking the convolution of the impulse
# response function and the forcing function set to the step function, you
# will end up with the integral of the impulse response function, and the
# integral of e to the power with negative terms will decay at the same
# relative rate.


# Questions

#Q1) Explain the result of the Final Value Theorem from Part 2 Task 2 in terms 
# of the physical circuit components.
#A1)  As time approaches infinity, you can measure longer wavelengths that
# will have their own location on the s domain. The s domain is the the inverse
# of the wavelength. As time approaches infinity. The circuit will get more
# attenuated from the resistor which means that the lower s values  will get
# smaller magnitudes.  The oscillation between the Capacitor and the inductor
# do not play in the long term because of that attenuation.
