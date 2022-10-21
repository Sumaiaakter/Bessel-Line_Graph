# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:14:50 2022

@author: Farhan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy as sc
import math

#from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.special import jn, jn_zeros
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig, ax = plt.subplots()
x_label=np.linspace(0,20,100)
for n in range(4):
    y_label=sc.special.jn(n,x_label)
    plt.plot(x_label,y_label,label=r'$J_ %s (X)$' %n)
plt.axhline(0,color='green',label='_nolegend_')
plt.grid()
plt.legend()
plt.xlabel('$X$',fontsize=15)
plt.ylabel('$J_m (X)$',fontsize=15)
plt.title(r'Bessel function $J_n(x)$',fontsize=15)


def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

anim = FuncAnimation(fig, frames=np.linspace(0, 2*np.pi, 128),init_func=init, blit=True)
#plt.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                    init_func=init, blit=True)


anim.save("line-up.gif", writer=PillowWriter(fps=24))
plt.show()
plt.savefig('Bessel Function.pdf')
print(x_label)
#print(y_label)

'''
clf;
x=[0:0.01:20]
alpha=0:5;
y=besselj(alpha,x);
plot2d(x,y,leg='J0@J1@J2@J3@J4@J5');
xlabel('x');
ylabel('Ja(x)');
xtitle('Some Bessel Functions of the first kind');
'''