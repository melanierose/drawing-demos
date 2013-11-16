

# import all the shit for the solving differential equations

import numpy as np
from scipy.integrate import odeint

def solvethings(k1,k2):

	# define system of eqns as dy/dt = f(y,t)
	def f(y,t):
		f0=-k1*y[0]
		f1=k1*y[0]-k2*y[1]
		f2=k2*y[1]
		return [f0,f1,f2]
	
	# set initial conditions
	y0 = [100,0,0]

	# define time interval to integrate
	t=np.linspace(0,60,1000)
	
	# solve the DEs
	soln = odeint(f, y0, t)
	E = soln[:,0]
	G = soln[:,1]
	S = soln[:,2]

	return [t,E,G,S]