from __future__ import division, print_function

from math import pi
from numpy import zeros
from scipy.integrate import ode

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
sigma = 0.001   #inverse Capillary number (characterize surdace tension)
nu = 1          #ratio of current loop radius to length of film


#functions
def f(x):
    return -3*nu^2*x/(1+nu^2*x^2)^4

def Q(x, h):
    return h^3/3*(sigma*d3hdx3(x)+1+lamb*f(x))

def d3hdx3(x):
    return

# Initialize grid
N = 200	#interior points
d = 1/N
time = 1000

x = zeros(3*N)
h = zeros(3*N) # Hold width of film at corresponding x index
for i in range(N):

    x(3*i) = d*((i+0.5)-0.5)
    x(3*i+1) = d*((i+1)-0.5)
    x(3*i+2) = d*((i+1.5)-0.5)


for i in range(3*N):
	h(i,0) = (x(i)-0.5)^2 #initial parabola

## Time evolution
dhdt = zeros(N,time)
#for each timestep
for t in range(0,time-1):
    #for each xi point
    for i in range(3*N):
        dhdt(i,t) = (Q(x(3*i+2), h(3*i+2)) - Q(x(3*i), h(3*i)))/d

	    f = (t,dhdt(i,t))
		#solve for h
		r = ode(f).set_integrator('vode', method='bdf', order=15)
		#r.set_initial_value(h(i, t), t)
		h(i,t+1) = r.integrate(r.t)


## Equilibrium analysis


