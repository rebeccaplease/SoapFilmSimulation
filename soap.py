# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:01:41 2015

@author: rebeccaplease
"""

from __future__ import division, print_function

from math import pi
from numpy import zeros
from pylab import plot, show

#Constants
#parameters used in the paper
g = 9.8         #gravity acceleration (m/s^2)
rho = 1.1       #density of solution (g/cm^3)
gamma = 0.042   #surface tension (N/m)
mu = 2          #viscosity (cP)
mu_0 = pi*4E-7  #magnetic permeability (N/A^2)
B_0 =  1684     #magnetic field strength (G)
chi_m = 0.05    #magnetic susceptibility
R = 4.4         #radius of current loop (cm)
h_b = 1         #film thickness at edge (mm)

# L = sqrt(gamma/(rho*g)) #vertical length of film
# nu = L/R

#time evolution simulation parameters
lamb = 1        #magnetic field strength
sigma = 0.001   #inverse Capillary number (characterize surface tension)
nu = 1          #ratio of current loop radius to length of film


# Initialize grid
N = 100	#interior points
d = 1/N
time = 10

size = 2*N
x = zeros(size+1, float)
h = zeros([size+1,time], float) # Hold width of film at corresponding x index
dhdt = zeros([size+1,time], float) # Hold derivatives at each time and point

#functions
# magnetic field and gravity forces
def f(i):
	return -3*nu**2*x[i]/(1+nu**2*x[i]**2)**4

# i is the index number being computed
# where i ranges from [2,N-2]
def Q(i, t):
	return h[i,t]**3/3*(sigma*d3hdx3(i,t)+1+lamb*f(i))

# index number from [2,N-2]
## use central difference to find third derivative for h

def d3hdx3(n,t):
	return (h[n+2,t]-2*h[n+1,t]+2*h[n-1,t]-h[n-2,t])/(2*d**3)
				
# use Adams bashforth method to solve dh/dt :D	
# use Euler's method for first step
def euler(n,t):
	return h[n,t] + d*dhdt[n,t]

# index number from [2,N-2]

def adamB2(n,t):
	return h[n-2,t] + 3/2*d*dhdt[n-1,t-1] - 1/2*d*dhdt[n-2,t-2]

#where c is the coefficient of the parabola (1+ for steeper starts)
def parabola(i,c):
	return c*(x[i]-0.5)**2+(1-0.25*c)
	
def parabolaDeriv(i,c):
	return c*2*(x[i]-0.5)

# fill array with x value points 
for i in range(size+1):
	x[i] = d*((i+0.5)-0.5)/2
	#x[3*i+1] = d*((i+1)-0.5)
	#x[3*i+2] = d*((i+1.5)-0.5)

# options for parabola 
# derivative points
for i in range(size+1):
	# boundary conditions - h always 1 at endpoints
	if i == 0:
		h[0,:] = 1
		dhdt[0,:] = 1*2*-0.5 
	elif i == size:
		h[size,:] = 1
		dhdt[size,:] = 1*2*0.5
	else:
		h[i,0] = parabola(i,1) #initial parabola with h = 1 at endpoints x = 0 and x = 1
		dhdt[i,0] = parabolaDeriv(i,1)


## Time evolution of soap film
#for each timestep
for t in range(0,time-1):
	#print("t:",t)
    #for each xi point
	for i in range(1,size-1):
		if i == 1:
			dhdt[i,t] = (Q(i+1,t)-0)/d
		elif i == size-2:
			dhdt[i,t] = (0-Q(i-1,t))/d
		#cant find 3rd derivs here
			
		else:
 			dhdt[i,t] = (Q(i+1,t)-Q(i-1,t))/d
	 #solve dhdt with Adams Bashforth
		# use Euler's method for first time step (need at least 2 points for 2 step AB)
		if t == 0:
			h[i,t+1] = euler(i,t)
		else:
#			if t==3:
#				print(i, adamB2(i,t))
			h[i,t+1] = adamB2(i,t)
	#h[i,]

#==============================================================================
# 	for i in range(1,N):
# 		#print(i)
# 		if i == 1:
# 			dhdt[i,t] = (Q(2*i+1,t)-0)/d
# 		elif i == N-1:
# 			dhdt[i,t] = (0-Q(2*i-1,t))/d
# 		# can't do 3rd derivative 
# 		else:
# 			dhdt[i,t] = (Q(2*i+1,t)-Q(2*i-1,t))/d
# 		# solve dhdt with Adams Bashforth
# 		# use Euler's method for first time step (need at least 2 points for 2 step AB)
# 		if t == 0:
# 			h[2*i,t+1] = euler(i,t)
# 			
# 		else:
# 			h[2*i,t+1] = adamB2(i,t)
# 			if i > 1:
# 				h[2*i-1,t+1] = (h[2*i-2,t+1]+h[2*i,t+1])/2
# 			if t==1:
# 				#print(i, adamB2(i,t))
# 				print(h[2*i-2,t+1],h[2*i,t+1])
# 				print(h[2*i-1,t+1])
#==============================================================================
				


plot(x[0:size:2],h[0:size:2,0])
plot(x,h[:,1])
plot(x[0:size:2],h[0:size:2,1])
plot(x[0:size:2],h[0:size:2,2])
plot(x[0:size:2],h[0:size:2,3])


#plot(x[0:size:2],h[0:size:2,time-1])
#plot(x,h[:,time-1])
show()