# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 9 #
# Due 28 Mar 2023 #
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

steps = 0.01
steps_0 = 0
steps_f = 2
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly



#====part1====


def fft(x,fs, ignore = False):
    N = len (x)
    X_fft = scipy.fftpack.fft(x)
    X_fft_shifted = scipy.fftpack.fftshift(X_fft)
    
    freq = np.arange (-N/2, N/2)*fs/N

    X_mag = np.abs(X_fft_shifted)/N
    X_phi = np.angle(X_fft_shifted)
    
    #----task 4----
    if (ignore):
        for i in range(len(X_mag)):
            if X_mag[i] < 1e-10:
                X_phi[i] = 0
    #---- end task 4 ----
    
    return freq, X_mag, X_phi




#----task 1----
# sig1 = cos(t, 1)

# sig1_fft, sig1_mag, sig1_phi = fft(sig1,1/steps)

# plt.figure(1)
# plt.plot(t, sig1)
# plt.xlabel('t [s]')
# plt.ylabel('x(t)')
# plt.title('Figure 1a: cos(2πt)')

# sig1_fft, sig1_mag, sig1_phi = fft(sig1,1/steps)

# plt.figure(2)
# plt.plot(sig1_fft, sig1_mag)
# plt.xlabel('f [Hz]')
# plt.ylabel('|X(ω)|')

# plt.figure(3)
# plt.plot(sig1_fft, sig1_phi)
# plt.xlabel('f [Hz]')
# plt.ylabel('∠X(f)')

# #----task 2----

# sig2 = 5*cos(t, 1)

# plt.figure(5)
# plt.plot(t, sig2, c="orange")
# plt.xlabel('t [s]')
# plt.ylabel('y(t)')
# plt.title('Figure 2a: 5 cos(2πt)')

# sig2_fft, sig2_mag, sig2_phi = fft(sig2,1/steps)

# plt.figure(6)
# plt.plot(sig2_fft, sig2_mag, c="orange")
# plt.xlabel('ω [f]')
# plt.ylabel('mag(ω)')
# plt.title('Figure 2b: magnitude of Fourier(5 cos(2πt))')

# plt.figure(7)
# plt.plot(sig2_fft, sig2_phi, c="orange")
# plt.xlabel('ω [f]')
# plt.ylabel('phi(ω)')
# plt.title('Figure 2c: phase of Fourier(5 cos(2πt))')

# #----task 3----
# sig3 = 2*cos(t, 2,2*2*(2*np.pi))+sin(t, 6,-3*6*(2*np.pi))*sin(t, 6,-3*6*(2*np.pi))

# plt.figure(8)
# plt.plot(t, sig3, c="red")
# plt.xlabel('t [s]')
# plt.ylabel('y(t)')
# plt.title('Figure 2a: 2 cos(2π 2t-2)+sin^2(2π 6t-3)')

# sig3_fft, sig3_mag, sig3_phi = fft(sig3,1/steps)

# plt.figure(9)
# plt.plot(sig3_fft, sig3_mag, c="red")
# plt.xlabel('ω [f]')
# plt.ylabel('mag(ω)')
# plt.title('Figure 2b: magnitude of Fourier(5 cos(2πt))')

# plt.figure(10)
# plt.plot(sig3_fft, sig3_phi, c="red")
# plt.xlabel('ω [f]')
# plt.ylabel('phi(ω)')
# plt.title('Figure 2c: phase of Fourier(5 cos(2πt))')



# #----task 5----
# T = 8
# w_0  = 2*np.pi/T

# a_0 = 0

# a_k = 0

# def b_k(k): 
#     return 2/(k*np.pi)*(1-np.power(-1,k))

# # print ("a_0", a_0)

# # a_1 = a_k
# # print ("a_1", a_1)

# # b_1 = b_k(1)
# # print ("b_1", b_1)

# # b_2 = b_k(2)
# # print ("b_2", b_2)

# # b_3 = b_k(3)
# # print ("b_3", b_3)


# def fourier_square(t,N):
#     y=np.zeros(t.shape)
    
#     for i in range(len(t)):
#         k = 1
        
#         y[i] = a_0
        
#         while k <= N:
#             y[i] += np.cos(k*w_0*i*steps) * a_k   +np.sin(k*w_0*i*steps) *b_k(k)
#             k += 1
        
        
#     return y

# steps_f = 16
# t = np.arange(steps_0,steps_f,steps)

# #f_1 = fourier_square(t,1)
# #f_3 = fourier_square(t,3)
# f_15 = fourier_square(t,15)
# #f_50 = fourier_square(t,50)
# #f_150 = fourier_square(t,150)
#f_1500 = fourier_square(t,1500)





# plt.figure(11)
# plt.plot(t, f_15, c="green")
# plt.xlabel('t [s]')
# plt.ylabel('y(t)')
# plt.title('Figure 2a: square wave to 15 terms')

# f_15_fft, f_15_mag, f_15_phi = fft(f_15,1/steps)

# plt.figure(12)
# plt.plot(f_15_fft, f_15_mag, c="green")
# plt.xlabel('ω [f]')
# plt.ylabel('mag(ω)')
# plt.title('Figure 2b: magnitude of Fourier(square wave to 15 terms)')

# plt.figure(13)
# plt.plot(f_15_fft, f_15_phi, c="green")
# plt.xlabel('ω [f]')
# plt.ylabel('phi(ω)')
# plt.title('Figure 2c: phase of Fourier(square wave to 15 terms)')





def signalFourierReport(timestamps, signalToCharacterize, fs, figureIndex, figureTitle, ignoreSmall=False):
    sig_fft, sig_mag, sig_phi = fft(signalToCharacterize,fs, ignoreSmall)
    
    plt.figure(figureIndex)
    
    #original signal
    ax1=plt.subplot2grid((3,2), (0,0), colspan=2)
    ax2=plt.subplot2grid((3,2), (1,0))
    ax3=plt.subplot2grid((3,2), (2,0))
    ax4=plt.subplot2grid((3,2), (1,1))
    ax5=plt.subplot2grid((3,2), (2,1))
    
    ax1.set_title('Figure ' + str(figureIndex) + ': ' + figureTitle)
    
    ax1.plot(timestamps, signalToCharacterize)
    ax1.set_xlabel('t [s]')
    ax1.set_ylabel('x(t)')

    #fourier transform magnitude
    ax2.stem(sig_fft, sig_mag)
    ax2.set_xlabel('f [Hz]')
    ax2.set_label('|X(ω)|')

    #fourier transform phase
    ax3.stem(sig_fft, sig_phi)
    ax3.set_xlabel('f [Hz]')
    ax3.set_ylabel('∠X(f)')
    
    
    #zoom setup
    middle_index = int(np.floor(len(sig_mag)/2))
    last_index = len(sig_mag) - 1
    
    domainMin = sig_fft[0]
    domainStart = domainMin
    for i in range(middle_index):
        if sig_mag[i] > 1e-10:
            domainStart = sig_fft[i]
            break
    
    domainMax = sig_fft[last_index]
    domainEnd = domainMax
    for i in range(middle_index):
        if sig_mag[last_index-i] > 1e-10:
            domainEnd = sig_fft[last_index-i]
            break
    
    domainWidth = domainEnd - domainStart
    
    domainStart = max([domainStart - domainWidth/2,domainMin])
    domainEnd = min([domainEnd + domainWidth/2,domainMax])
    
    
    
    #fourier transform magnitude zoomed
    ax4.stem(sig_fft, sig_mag)
    ax4.set_xlabel('f [Hz]')
    ax4.set_ylabel('|X(ω)|')
    ax4.set_xlim(domainStart,domainEnd)
    
    
    #fourier transform phase zoomed
    ax5.stem(sig_fft, sig_phi)
    ax5.set_xlabel('f [Hz]')
    ax5.set_ylabel('∠X(f)')
    ax5.set_xlim(domainStart,domainEnd)
    
    
    plt.tight_layout()
    return




#----task1----
fs = 100#1/steps

sig1 = cos(t, 1)
signalFourierReport(t,sig1,fs, 1, 'cos(2πt) with phase noise', False)

#----task2----
sig2 = 5*sin(t, 1)
signalFourierReport(t,sig2,fs, 2, '5cos(2πt) with phase noise', False)

#----task3----
sig3 = 2*cos(t, 2,2*2*(2*np.pi))+sin(t, 6,-3*6*(2*np.pi))*sin(t, 6,-3*6*(2*np.pi))

signalFourierReport(t,sig3,fs, 3, '2cos((2π·2t)-2)+sin²((2π·6t)-3) with phase noise', False)

#----task4----
signalFourierReport(t,sig1,fs, 4, 'cos(2πt) without phase noise', True)
signalFourierReport(t,sig2,fs, 5, '5cos(2πt) without phase noise', True)
signalFourierReport(t,sig3,fs, 6, '2cos((2π·2t)-2)+sin²((2π·6t)-3) without phase noise', True)

#----task5----
T = 8
w_0  = 2*np.pi/T

a_0 = 0

a_k = 0

def b_k(k): 
    return 2/(k*np.pi)*(1-np.power(-1,k))


def fourier_square(t,N):
    y=np.zeros(t.shape)
    
    for i in range(len(t)):
        k = 1
        
        y[i] = a_0
        
        while k <= N:
            y[i] += np.cos(k*w_0*i*steps) * a_k   +np.sin(k*w_0*i*steps) *b_k(k)
            k += 1
        
        
    return y

steps_f = 16
t = np.arange(steps_0,steps_f,steps)

f_15 = fourier_square(t,15)

signalFourierReport(t,f_15,fs, 7, 'Fourier Series of square wave to 15 terms without phase noise', True)



# Questions
#Q2) What difference does eliminating the small phase magnitudes make?
#A2) eliminating the noise in the phase (which is caused by boolean algebra 
# error when the computer calculates it) allows us to see the phases of the
# frequencies that have a significant effect.

#Q3) Verify your results from Tasks 1 and 2 using the Fourier transforms of
# cosine and sine. Explain why your results are correct. You will need the
# transforms in terms of Hz, not rad/s. For example, the Fourier transform of
# cosine (in Hz) is:
#ℱ{cos(2 π f_t)} = 1/2 [δ(f-f_0)+δ(f+f_0)]
#A3)#from task 1, there are 0.5 tall spikes at -1 and 1, and the phases at -1
# and 1 are 0.
#0.5 δ(f=1)+ 0.5 δ(f-1) = 0.5 [δ(f=1)+δ(f-1)] = ℱ{cos(2 π 1)}

#from task 2, there are 2.5 tall spikes at -1 and 1, and the phases are at
# about 1.5 and -1.5 respectively (1.5 is approximately pi/2)
#2.5 j δ(f+1) - 2.5 j δ(f-1) = j2.5 [δ(f+1)-δ(f-1)] = ℱ{5sin(2 π 1)}


#Q5) Leave any feedback on the clarity of lab tasks, expectations, and
# deliverables.
#A5) This lab was pretty strait forward, other than "figure out how to code the
# presentation plot".  I had to learn about Axes and Subplots to get it to
# present right.
# Also, Question 3 wants us to  verify results from Task 1 and 2, which sure
# could be done, but with the phase noise, it was slightly confusing even
# though only the phase at the specific locations are used.



