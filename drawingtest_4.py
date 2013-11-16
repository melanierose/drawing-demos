# import all the shit for the solving differential equations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from pylab import show
import matplotlib as mpl


# define rates
k1=0.05	#ER exit rate constant (in min -1)
k2=.05	#Golgi to SG rate constant (in min -1)

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

# plot results as the first of 2 subplots
F  = plt.figure()
plt.subplot(1, 2, 1)
plt.plot(t, E, label='ER')
plt.plot(t, G, label='Golgi')
plt.plot(t, S, label='SG')
plt.xlabel('time (min)')
plt.ylabel('% of total pulse')
plt.title('modeling transport ER -> Golgi -> SG', size='small')
plt.legend(loc=0)

#figure out the vectors
#want to use E (ER) vector as the scale because it has the highest %total pulse
#to verify this:
#print np.max(E), np.max(G), np.max(S)

#set the max, min of the scale
vmax, vmin = np.max(E), np.min(E)

# ax1 is the scale bar for the second plot
#orient it so it's over that part of the final figure
#Add an axes at position rect [left, bottom, width, height] 
ax1 = F.add_axes([0.5, .95, 0.46, 0.03])

# Set the colormap and norm to correspond to the data for which
# the colorbar will be used.
cmap = mpl.cm.hot
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,
                                   norm=norm,
                                   orientation = 'horizontal'
                                   )
cb1.set_label('percent of total pulse', size='small')

# is it possible to put a win from graphics.py into a subplot?
# maybe no

# this is a placeholder
"""
plt.subplot(1,2,2)
plt.plot(G,E)
"""

# this is the real deal, in a separate window (graphwin)
"""
from graphics import *
def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    message = Text(Point(win.getWidth()/2, 20), 'click some things')
    message.draw(win)
    win.getMouse()
    win.close()
"""

# alternative: concatenate vectors into an array
# plot the array with values as intensities
# in a separate figure

imj = [E,G]
imj = np.vstack((imj,S))

plt.matshow(imj, fignum=2, cmap=cmap, aspect='auto')

# take show vectors and normalize them so they can be used to adjust a color or alpha or something
imnorm = plt.Normalize(imj)



show(F)


