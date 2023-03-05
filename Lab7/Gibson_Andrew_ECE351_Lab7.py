# -*- coding: utf-8 -*-
################################################################
# #
# Andrew Gibson #
# ECE 351 lab, Section 53 #
# Lab 7 #
# Due 07 Mar 2023 #
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


steps = .01
steps_0 = 0
steps_f = 20
t = np.arange(steps_0,steps_f,steps)
t_offset = min(round(steps_0/steps),0)#offset is in order for zero to work correctly



#====part1====

#----task1----
#G(s) = (s+9)/((s^2-6s-16)(s+4))
#G(s) = A/(s+4) + B/(s-8) + C/(s+2)

#A=(s+9)/((s-8)(s+2)) |_n=-4 = ((-4)+9)/(((-4)-8)((-4)+2) = 1/24
#B=(s+9)/((s+4)(s+2)) |_n=8 = ((8)+9)/(((8)+4)((8)+2)) = 17/120
#C=(s+9)/((s+4)(s-8)) |_n=-2 = ((2)+9)/(((2)+4)((2)-8)) = -11/36

#G(s) =  (1/24)/(s+4) + (17/120)/(s-8) + (-11/36)/(s+2)
#poles are -4, 8, -2
#zeroes are -9


#A(s) = (s+4)/(s^2+4s+3)
#A(s) = B/(s+3) + C/(s+1)

#B=(s+4)/(s+1) |_n=-3 = ((-3)+4)/((-3)+1) = 1/2
#C=(s+4)/(s+3) |_n=-1 = ((-1)+4)/((-1)+3) = 3/2

#A(s) = (1/2)/(s+3) + (3/2)/(s+1)
#poles are -1, -3
#zeroes are -4 


#B(s) = s^2+26s+168
#B(s) = (s+12)(s+14)

#there are no poles
#zeroes are -12 and -14


#----task2----
G_zp = sig.tf2zpk([1,9],[1,-6+1*4,-16-6*4,-16*4])

A_zp = sig.tf2zpk([1,4],[1,4,3])

B_zp = sig.tf2zpk([1,26,168],[1])

B_roots = np.roots([1,26,168])


print("---Part 1 Task 2: poles and zeroes---")


print("using \"scipy.signal.tf2zpk()\"")
print("G(s)", G_zp)
print("A(s)", A_zp)
print("B(s)", B_zp)
print("\nusing \"numpy.roots()\"")
print("B(s)", B_roots)


#----task3----
#                Z(s)
#X(s) ──> [A(s)] ───> +o ──> [G(s)] ───> Y(s)

#Y = G*A*X

#Y(s) = ((s+9)/((s+4)(s-8)(s+2)))*((s+4)/((s+3)(s+1)))*X(s)
#Y(s) = ((s+9)(s+4))/((s+4)(s-8)(s+2)(s+3)(s+1))*X(s)

#Y(s) = (s+9)/((s-8)(s+2)(s+3)(s+1))*X(s)


#typo in instructions, we  were not suppose to do this
    #Y(s)/X(s) = (s+9)/((s-8)(s+2)(s+3)(s+1))

    #A = (s+9)/((s+2)(s+3)(s+1)) |_n=8 = 17/990
    #B = (s+9)/((s-8)(s+3)(s+1)) |_n=-2 = 7/10
    #C = (s+9)/((s-8)(s+2)(s+1)) |_n=-3 = 6/-22 = -3/11
    #D = (s+9)/((s-8)(s+2)(s+3)) |_n=-1 = 8/-18 = -4/9

    #H(s) = (17/990)/(s-8)+(7/10)/(s+2)+ (-3/11)/(s+3)+(-4/9)/(s+1)

    #h(t) = ((17/990)e^(8t) + (7/10)e^(-2t)+(-3/11)e^(-3t)+(-4/9)e^(-1t))u(t)

    #y(t) = ((17/990)e^(8t) + (7/10)e^(-2t)+(-3/11)e^(-3t)+(-4/9)e^(-1t))u(t)x(t)



#----task4----
# the open-loop response is not stable because of the (s-8) term in the 
# denominator. when converting that term to time domain, there will be an
# e^(-(-8)t), and e^(8t) does not converge to a finite number as t aproaches 
# infinity



#----task5----
#Y(s) = (s+9)/((s-8)(s+2)(s+3)(s+1))*X(s)
num = [1,9]
den = sig.convolve([1,-6,-16],[1,4,3])
#A_star_B = sig.convolve(G_zp, A_zp)


print("\n\n---Part 1 Task 5: expanding num and den---")

print("num", num)
print("den", den)

# y = (s+9) / (s^5 - 2s^3 - 37s^2 - 82s - 48)

t_AG_step, y_AG_step = sig.step((num,den),T=t)

plt.figure(0)
plt.plot(t_AG_step, y_AG_step)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 2: Part 1, Step Response of open-loop')


#----task6----
# The result of task 5 corresponds to the results of task4 as the graph grows 
# exponentially which as t becomes large.



#====Part2====

#----task1----

#                Z(s)
#X(s) ──> [A(s)] ───> +o ──> [G(s)] ───> Y(s)
#                     ^-             |
#                     |              |
#                     └── [B(s)] <───┘

# Y = G*E
# E=A*X-B*Y

# A*X-B*Y = Y/G
# A*X = Y/G+B*Y
# G*A*X = Y+G*B*Y
# G*A*X = Y(1+G*B)
# Y = (G*A*X)/(1+G*B)
# H = (G*A)/(1+G*B)


#H = (numG/denG*numA/denA)/(1+numG/denG*numB/denB)
#H = ((numG*numA)/(denG*denA))/(1+(numG*numB)/(denB*denG))
#H = ((numG*numA)(denB*denG)/(denG*denA))/((denB*denG)+(numG*numB))
#H = ((numG*numA)(denB*denG))/((denB*denG)(denG*denA)+(numG*numB)(denG*denA))
#H = (numG*numA*denB*denG)/((denB*denG*denG*denA)+(numG*numB*denG*denA))
#H = (numG*numA*denB)/((denB*denG*denA) + (numG*numB*denA))


#----task2----

numA = [1,4]
denA = [1,4,3]
numB = [1,26,168]
denB = [1]
numG = [1,9]
denG = [1,-2,-37,-82,-48]

f_num = sig.convolve(sig.convolve(numG,numA),denB)
f_den1 = sig.convolve(sig.convolve(denB,denG),denA)
f_den2 = sig.convolve(sig.convolve(numG,numB),denA)


print("\n\n---Part 2 Task 2: solving thin---")

print("f_num", f_num)
print("f_den1", f_den1)
print("f_den2", f_den2)


def addCoefficients(a,b):
    if len(a) < len(b):
        c = np.flip(b.copy())
        c[:len(a)] += np.flip(a)
        return np.flip(c)
    else:
        c = np.flip(a.copy())
        c[:len(b)] += np.flip(b)
        return np.flip(c)

f_den = addCoefficients(f_den1,f_den2)
print("f_den", f_den)


f_zp = sig.tf2zpk(f_num,f_den)
print("f_zp", f_zp)


# [(s+9)(s+4)]/
# [(s-(4.9403119+6.14882075j))(s-(4.9403119-6.14882075j))
#  (s-(-4.4403119+1.9532165j))(s-(-4.4403119-1.9532165j))
#  (s+3)(s+1) ]



#----task3----
#because there are complex roots, there is no convergance to a single value,
#however, those roots could explode.

#take the inverse laplace of the term 1/(s+a+bj)
#e^(-(a+bj)t)
#e^(-at)*e^(-bjt)
#e^(-at)*(e^(jt))^(-b)
#e^(-at)*(cos(t)+jsin(t))^(-b)

# therefore as long as the real components of the zeros are all negative, then
# there would be stability.
# This system is still unstable even with the feedback, and it will oscilate
# in which direction it is unstable


#----task4----

t_AGnB_step, y_AGnB_step = sig.step((f_num,f_den),T=t)

plt.figure(1)
plt.plot(t_AGnB_step, y_AGnB_step)
plt.xlabel('t [s]')
plt.ylabel('y(t)')
plt.title('Figure 5: Part 2, Step Response of closed-loop')


#----task5----
# The result of task 4 corresponds to the results of task3 as the graph grows 
# exponentially larger (albeit periodically) as t becomes large.




# Questions
#Q1) In Part 1 Task 5, why does convolving the factored terms using 
# scipy.signal.convolve() result in the expanded form of the numerator and 
# denominator? Would this work with your user-defined convolution function from
# Lab 3? Why or why not? 
#A1) the scipy.signal.convolve() function works with the coefficients of a
# numerator and denomenator in the s domian.  It would not work in the time 
# domain.  You can do a discrete convolution in the time domain with 
# numpy.convolve. The user defined function in Lab 3 is also a descrete 
# convolution in the time domain.  Scipy.signal.convolve and the user defined 
# function in lab 3 are not compatible.

#Q2) Discuss the difference between the open- and closed-loop systems from Part
# 1 and Part 2. How does stability differ for each case, and why?
#A2) The open end system  has a signal going one way and no feed back, however 
# the output is unstable, the closed system  has a feedback loop that is also 
# unstable but does not converge as t approaches infinity.

#Q3) What is the difference between scipy.signal.residue() used in Lab 6 and 
# scipy.signal.tf2zpk() used in this lab?
#A3) the function scipy.signal.residue() numerator and denominator coefficients 
# in the s domain and returns the partial-fraction expansion with the residue
#  corresponding to the poles, the poles, and any standalone coefficients. the
# function scipy.signal.tf2zpk also takes numerator and denominator coefficients
# but returns the values of s to cause it to equal zero (zeroes), the values of
# s where it is undefined (poles), and the gain.

#Q4) Is it possible for an open-loop system to be stable? What about for a 
#closed-loop system to be unstable? Explain how or how not for each.
#A4) it is possible for an open-loop to system to be stable as it would need a
# term that had a positive pole. Same goes for closed-loop systems.

#Q5) Leave any feedback on the clarity/usefulness of the purpose, deliverables,
# and expectations for this lab.
#A5) Some time was wasted calculating y(t) because of a type in the procedure.
# Also it was unclear if we were suppose to work only in the s domain.
# It is also unclear how to add the coefficients together two numpy.arrays,which 
# is what scipy.signal uses that are of different lengths. The feedback system had such a case where we needed to do that to get the terms.



