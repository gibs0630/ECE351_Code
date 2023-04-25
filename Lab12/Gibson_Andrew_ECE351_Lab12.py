# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 12 #
# Due 25 Apr 2023 #
# Final Project; Filter Design #
# https://github.com/gibs0630/ECE351\_Code #
# https://github.com/gibs0630/ECE351\_Reports #
# #
################################################################


# the other packages you import will go here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy.signal as sig
import scipy as scipy
import control as con

# load input signal
df = pd.read_csv ('NoisySignal.csv')
#df.fillna(0, inplace = True)
#df = df.replace(np.nan, 0)

t = df['0'].values
sensor_sig = df['1'].values

#sensor_sig = sensor_sig.replace(np.nan, 0)
t_step = t[1]-t[0]

plt.figure(figsize = (10 , 7) )
plt.plot(t, sensor_sig )
plt.grid()
plt.title('Figure 1: Noisy Input Signal')
plt.xlabel('Time[s]')
plt.ylabel('Amplitude[V]')
plt.show()


# --- ---

def fft(x, fs, ignore = False):
    N = len (x)
    X_rfft = scipy.fft.rfft(x)
    #X_fft_shifted = scipy.fftpack.fftshift(X_fft)
    
    #freq = np.arange (-N/2, N/2)*fs/N
    freq = scipy.fft.rfftfreq(N, t_step)
    
    X_mag = np.abs(X_rfft)/N
    X_phi = np.angle(X_rfft)
    
    if (ignore):
        for i in range(len(X_mag)):
            if X_mag[i] < 1e-10:
                X_phi[i] = 0
                
    return freq, X_mag, X_phi

sig_freq, sig_mag, sig_phi = fft(sensor_sig,1/t_step)

plt.figure(2)
plt.semilogx(sig_freq, sig_mag)
plt.xlabel('f [Hz]')
plt.ylabel('|X(ω)|')
plt.title('Figure 2: Fourier Transform, magnitude')

plt.figure(3)
plt.semilogx(sig_freq, sig_phi*180/np.pi)
plt.xlabel('f [Hz]')
plt.ylabel('∠X(f) [deg]')
plt.title('Figure 3: Fourier Transform, phase')

plt.figure(4)
plt.semilogx(sig_freq, sig_mag)
plt.xlabel('f [Hz]')
plt.ylabel('|X(ω)| ')
plt.title('Figure 4: Zoomed Fourier Transform, magnitude')
plt.xlim(1600,2200)


plt.figure(5)
plt.semilogx(sig_freq, sig_phi*180/np.pi)
plt.xlabel('f [Hz]')
plt.ylabel('∠X(f) [deg]')
plt.title('Figure 5: Zoomeed Fourier Transform, phase')
plt.xlim(1600,2200)

plt.figure(6)
plt.semilogx(sig_freq, sig_mag)
plt.xlabel('f [Hz]')
plt.ylabel('|X(ω)| ')
plt.title('Figure 6: Nearby Unwanted Signals Below Position Measurement')
plt.xlim(1,1800)

plt.figure(7)
plt.semilogx(sig_freq, sig_mag)
plt.xlabel('f [Hz]')
plt.ylabel('|X(ω)| ')
plt.title('Figure 7: Near by Unwanted signals Above Position Measurement')
plt.xlim(2000,6500)


#---the filter---
# (K bw s)/ (s^2 + bw*s + w_0^2)

K = 1.0#gain
bw = 769.0#bandwidth
w_0 = 1900.0#center frequency

#domain
s_steps = 100
s_steps_0 = 1e3
s_steps_f = 1e7
s = np.arange(s_steps_0,s_steps_f,s_steps)


#bode
plt.figure(8)
sys = con.TransferFunction([K*bw,0],[1, bw, np.power(w_0,2)])

H = con.bode (sys, sig_freq, dB=True, Hz=True, deg=True, plot=True)
plt.suptitle('Figure 8: Bode plot of filter')


#find magnitude and phase given freq of a control.bode output

def findMP(H,f):
    if (type(H) != tuple):
        raise Exception("missing tuple from the return of the function \"control.bode\"")
        return
    if (f < float(H[2][0]) or f > float(H[2][-1])):
        raise Exception("f, " + str(f) + "Hz, is outside the domain of H \"[" + str(H[2][0]) +": "+str(H[2][-1]) +"]\"")
        return
    
    i_low = 0
    i_high = len(H[2])-1
    for i in range(len(H[2])-1):
        if ((float(H[2][i]) <= f) and (float(H[2][i_low]) < float(H[2][i]))):
            i_low = i
        if ((H[2][i] >= f) and (float(H[2][i_high]) > float(H[2][i]))):
            i_high = i
    
    m = (float(H[0][i_low]) + float(H[0][i_high]))/2
    p = (float(H[1][i_low]) + float(H[1][i_high]))/2
    
    #print(float(H[2][i_low]),i_low, float(H[2][i_high]), i_high)
    
    #print(float(H[2][i_low]),f, float(H[2][i_high]))
    return m, p
    


def dB_to_lin(x_dB):
    return np.power(10,x_dB/20)

H_60, _ = findMP(H,60)
H_1800, _ = findMP(H,1800)
H_2000, _ = findMP(H,2000)
H_6000, _ = findMP(H,6000)
H_100000, _ = findMP(H,100000)

print("at 60Hz, H = " + str(H_60) + ", within spec? " + str(H_60 < dB_to_lin(-30))  )
print("at 1800Hz, H = " + str(H_1800) + ", within spec? " + str(H_1800 > dB_to_lin(-0.3))  )
print("at 2000Hz, H = " + str(H_2000) + ", within spec? " + str(H_2000 > dB_to_lin(-0.3))  )
print("at 6000Hz, H = " + str(H_6000) + ", within spec? " + str(H_6000 < dB_to_lin(-21))  )
print("at 1000000Hz, H = " + str(H_100000) + ", within spec? " + str(H_100000 < 0.05 )  )

plt.figure(9)
#plt.semilogx(sig_freq, sig_mag, "#eeeeaa")
plt.loglog(H[2], H[0])
plt.xlabel('f [Hz]')
plt.ylabel('|H(ω)|')
plt.title('Figure 9: Filter, magnitude')


freq_of_importance = [60, 1800, 2000, 6000, 100000]
gain_of_importance = [dB_to_lin(-30),dB_to_lin(-0.3),dB_to_lin(-0.3),dB_to_lin(-21), 0.05]
color_of_importance = ['ro','ro','ro','ro','ro']
    
if (H_60 < dB_to_lin(-30)):
    color_of_importance[0] = 'go'
    
if (H_1800 > dB_to_lin(-0.3)):
    color_of_importance[1] = 'go'
    
if (H_2000 > dB_to_lin(-0.3)):
    color_of_importance[2] = 'go'
    
if (H_6000 < dB_to_lin(-21)):
    color_of_importance[3] = 'go'
    
if (H_100000 < 0.05 ):
    color_of_importance[4] = 'go'
    
plt.loglog(freq_of_importance[0],gain_of_importance[0], color_of_importance[0])
plt.loglog(freq_of_importance[1],gain_of_importance[1], color_of_importance[1])
plt.loglog(freq_of_importance[2],gain_of_importance[2], color_of_importance[2])
plt.loglog(freq_of_importance[3],gain_of_importance[3], color_of_importance[3])
plt.loglog(freq_of_importance[4],gain_of_importance[4], color_of_importance[4])
    



def searchSolution(mbw,mw_0):
    for bw in range(1,mbw,1):
        print(str(bw))
        for w_0 in range(1000,2000,1):
            sys = con.TransferFunction([bw,0],[1, bw, np.power(w_0,2)])
            
            if (float(sys(60)) <= dB_to_lin(-30)):
                if (float(sys(1800)) >= dB_to_lin(-0.3)):
                    if (float(sys(2000)) >= dB_to_lin(-0.3)):
                        if (float(sys(6000)) <= dB_to_lin(-21)):
                            # if (float(sys(100000)) <= 0.05):
                            print("found solution; bw = " + str(bw) + "; w_0 = " + str(w_0) )
                            return

#searchSolution(1000,1900)
# did not find anything



plt.figure(10)
plt.semilogx(sig_freq, sig_mag*H[0])
plt.xlabel('f [Hz]')
plt.ylabel('V')
plt.title('Figure 10: Filtered signal')


plt.figure(11)
myplt = plt.semilogx(sig_freq, sig_mag*H[0]>0.05)
plt.xlabel('f [Hz]')
plt.title('Figure 11: Range with signal > 0.05V')
ax = plt.gca();
ax.get_yaxis().set_visible(False)

plt.figure(13)
system = ([K*bw,0],[1, bw, np.power(w_0,2)])
t, yout = scipy.signal.impulse(system, T = t)
plt.plot(t, yout )
plt.title('Figure 13: Impulse Response of Filter')
plt.xlabel('Time[s]')
plt.ylabel('Amplitude[V]')
plt.show()

plt.figure(14)
out_sig = sig.fftconvolve(yout, sensor_sig, "same")
plt.plot(t, out_sig * t_step )
plt.title('Figure 14: Output Signal')
plt.xlabel('Time[s]')
plt.ylabel('Amplitude[V]')
plt.show()

# --- Circuit ---
# (769 s)/ (s^2 + 769*s + 1900^2)
# this filter can be created with the following relations with an LCR series circuit where output is around the resistor
# (R/L s) / (s^2 + R/L s + 1 / (LC))

#1/(LC) = 1900^2
#R/L = 769

#lets set R = 1k Ohm
#C = 2.1301939058171745152354570637119e-7 F
#L = 1.3003901170351105331599479843953 H

#  +--L--C--+---
# (~)       R
#  +--------+---


# Questions

#Q1) Earlier this semester, you were asked what you personally wanted to get out of taking this course. Do you feel like that personal goal was met? Why or why not?
#A1) I have met my goals of getting some exploration on applications and a passing class.  I know how to create a program that will do digital filtering.

#Q2) Please fill out the course feedback survey, I will read every word and very much appreciate the feedback.
#A2) It is done.

#Q3) Good luck in the rest of your education and career!
#A3) Thank you.
