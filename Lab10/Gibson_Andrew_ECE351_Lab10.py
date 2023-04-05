# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 10 #
# Due 4 Apr 2023 #
# Frequency Response #
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
R = 1000
L = 27e-3
C = 100e-9


def gainofH(s):
    y=np.zeros(s.shape)
    
    for i in range(len(s)):
        
        y[i]=((s[i])/(R*C))/(
            np.sqrt(
                np.power(s[i],4)   +   (1/(R*R*C*C)-2/(L*C))*np.power(s[i],2)   +   (1/(L*L*C*C))
            )
        )
    return y


gainH = gainofH(s)
plt.figure(2)
plt.semilogx(s,gainH)
plt.ylabel('gain')
plt.xlabel('f(rad/s)')
plt.title('Figure 1a: Equation, Gain')

def phaseofH(s):
    y=np.zeros(s.shape)
    
    for i in range(len(s)):
        
        y[i]=np.pi/2 - np.arctan2(s[i]/(R*C),1/(L*C)-s[i]*s[i])
    return y
    

phaseH = phaseofH(s)
plt.figure(3)
plt.semilogx(s,phaseH)
plt.ylabel('phase')
plt.xlabel('f(rad/s)')
plt.title('Figure 1b: Equation, Phase')

#---task 2---

w, mag, phase = sig.bode(([1/(R*C),0],[1,1/(R*C),1/(L*C)]),s)

mag = gainofH(w)
plt.figure(4)
plt.semilogx(s,gainH)
plt.ylabel('gain')
plt.xlabel('f(rad/s)')
plt.title('Figure 2a: Bode in Rad/s, Gain')

plt.figure(5)
plt.semilogx(w,phase)
plt.ylabel('phase')
plt.xlabel('f(rad/s)')
plt.title('Figure 2b: Bode in Rad/s, Phase')


#---task 3---

plt.figure(6)
import control as con # this package is not included in the Anaconda
                      # distribution , but should have been installed in lab 0

sys = con.TransferFunction([1/(R*C),0],[1,1/(R*C),1/(L*C)])
_ = con.bode (sys, s, dB=True, Hz=True, deg=True, Plot=True)
 # use _ = ... to suppress the output
plt.suptitle('Figure 3: Bode in Hz, Phase')


#===part 2===

#---task 1---
def genx(t):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        y[i] = np.cos(2*np.pi*100*t[i])+np.cos(2*np.pi*3024*t[i])+np.sin(2*np.pi*50000*t[i])
    return y

x = genx(t)

plt.figure(7)
plt.plot(t,x)
plt.ylabel('x(t)')
plt.xlabel('t(s)')
plt.title('Figure 4: cos(2π*100t)+cos(2π*3024t)+sin(2π*50000t)')


#---task 2---
zdomainHb, zdomainHa = sig.bilinear([1/(R*C),0],[1,1/(R*C),1/(L*C)],1/steps)


#---task 3---
y = scipy.signal.lfilter(zdomainHb, zdomainHa, x)

#---task 4---
plt.figure(8)
plt.plot(t,y)
plt.ylabel('y(t)')
plt.xlabel('t(s)')
plt.title('Figure 5: [cos(2π*100t)+cos(2π*3024t)+sin(2π*50000t)]★h(t)')



# Questions
#Q1) Explain how the filter and filtered output in Part 2 makes sense given the Bode plots from Part 1. Discuss how the filter modifies specific frequency bands, in Hz.
#A1) The filter makes since when consulting the bode plot. in the original signal, there were three super-positioned sinusoidal with different frequencies. According to the bode plot for magnitude, both the 100Hz and 50000Hz would be attenuated, reducing them to -30 dB relative to the input signal.

#Q2) Discuss the purpose and workings of scipy.signal.bilinear() and scipy.signal.lfilter()
#A2) The scipy.signal.biliner function is suppose to convert a signal from the s-domain to the z domain, where the z-domain is composed of discrete timestamps instead of a temporal continuum. The scipy.signal.lfilter function is suppose to do discrete convolution but with a time-domain input and a z-domain filter and then output the filtered output in the time-domain.

#Q3) What happens if you use a different sampling frequency in scipy.signal.bilinear() than you used for the time-domain signal?
#A3) If a different sampling frequency is used, then the function may not attenuate certain signals, or it may temporal stretch a signal, or produce artifacts (such as oscillating amplitude for a certain frequency, a wah-wah like effect). For example if the sampling frequency was 3 times that of the input signal sampling frequency then something like this could occur.

zdomainHb2, zdomainHa2 = sig.bilinear([1/(R*C),0],[1,1/(R*C),1/(L*C)],3/steps)

y2 = scipy.signal.lfilter(zdomainHb2, zdomainHa2, x)
plt.figure(9)
plt.plot(t,y2)
plt.ylabel('y(t)')
plt.xlabel('t(s)')
plt.title('Figure 6: Desynced Signal')


#Q4) Leave any feedback on the clarity of lab tasks, expectations, and deliverables
#A4) There was some minor clarity issue with what the variable fs was.

