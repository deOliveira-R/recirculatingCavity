#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 07:53:06 2018

@author: deoliveira_r
"""
from math import tau
import numpy as np

from sympy import symbols, sin, cos, exp, sqrt, diff, init_printing, init_session, trigsimp, simplify
from sympy.vector import CoordSys3D, gradient, divergence
from sympy.plotting import plot3d, plot
#init_printing()
#init_session()

pressure = 1e5
density = 1000
dyn_viscosity = 50

x, y = symbols('x y')
P, rho, mu = symbols('P rho mu')

vel = (sin(x)*cos(y),
       -cos(x)*sin(y),
       0)
velMag = sqrt(sum(component**2 for component in vel))
press = P + rho*(cos(x)**2 + cos(y)**2)/2

velocity_x_field = plot3d(vel[0], (x, 0, tau/2), (y, 0, tau/2), xlabel='X', ylabel='Y', show=False)
velocity_y_field = plot3d(vel[1], (x, 0, tau/2), (y, 0, tau/2), show=False)
velocity_mag_field = plot3d(velMag, (x, 0, tau/2), (y, 0, tau/2), show=False)
velocity_mag_section = plot(velMag.subs(y, tau/4), (x, 0, tau/2), show=False)
pressure_field = plot3d(press.subs([(P, pressure), (rho, density), (mu, dyn_viscosity)]), (x, 0, tau/2), (y, 0, tau/2), show=False)
pressure_field_section = plot(press.subs([(y, tau/4), (P, pressure), (rho, density), (mu, dyn_viscosity)]), (x, 0, tau/2), show=False)

plots = [velocity_x_field, velocity_y_field, velocity_mag_field, velocity_mag_section, pressure_field, pressure_field_section]

# CHECKING NS EQUATION

advectionX = rho*(vel[0]*diff(vel[0], x) + vel[1]*diff(vel[0], y))
diffusionX = - mu*(diff(vel[0], x, 2) + diff(vel[0], y, 2))
stressesX =  diff(press, x)
print("\nThe advective term for X is:", simplify(advectionX))
print("The diffusive term for X is:", simplify(diffusionX))
print("The stress term for X is:", simplify(stressesX))

print("\nTotal source X:", simplify(advectionX+diffusionX+stressesX))

advectionY = rho*(vel[0]*diff(vel[1], x) + vel[1]*diff(vel[1], y))
diffusionY = - mu*(diff(vel[1], x, 2) + diff(vel[1], y, 2))
stressesY =  diff(press, y)
print("\nThe advective term for Y is:", simplify(advectionY))
print("The diffusive term for Y is:", simplify(diffusionY))
print("The stress term for Y is:", simplify(stressesY))

print("\nTotal source Y:", simplify(advectionY+diffusionY+stressesY))


#R = CoordSys3D('R')
#vel = sin(R.x)*cos(R.y)*R.i \
#    - cos(R.x)*sin(R.y)*R.j \
#    + 0*R.k
#pressu = P - rho*(cos(R.x)**2+cos(R.y)**2)/2 + 2*mu*cos(R.x)*cos(R.y)
#
#print(vel.components, type(vel))
## print("\nThe gradient of the velocity is:", gradient(vel))
#print("\nThe dyadic produc is:", vel|vel)
#dya = divergence(vel|vel)
#print("\nThe divergence of the dyadic is:", type(dya))
#print("\nThe addition is:", vel+divergence(vel|vel))
#print(vel.magnitude())






#navier_stokes_X = rho*(velX*diff(velX, x) + velY*diff(velX, y)) \
#              - mu*(diff(velX, x, 2) + diff(velX, y, 2)) \
#              - diff(P, x)
#              
#navier_stokes_Y = rho*(velX*diff(velY, x) + velY*diff(velY, y)) \
#              - mu*(diff(velY, x, 2) + diff(velY, y, 2)) \
#              - diff(P, y) 
#              
#convectionX = rho*(velX*diff(velX, x) + velY*diff(velX, y))
#diffusionX = - mu*(diff(velX, x, 2) + diff(velX, y, 2))
#stressX = - diff(P, x)
#
#print(convectionX.subs([(velX, velX_expr), (velY, velY_expr)]))
#print(diffusionX.subs([(velX, velX_expr), (velY, velY_expr)]))
#print(stressX.subs([(velX, velX_expr), (velY, velY_expr)]))
#
#convectionY = rho*(velX*diff(velY, x) + velY*diff(velY, y))
#diffusionY = - mu*(diff(velY, x, 2) + diff(velY, y, 2))
#stressY = - diff(P, y)
#
#print(convectionY.subs([(velX, velX_expr), (velY, velY_expr)]))
#print(diffusionY.subs([(velX, velX_expr), (velY, velY_expr)]))
#print(stressY.subs([(velX, velX_expr), (velY, velY_expr)]))
#
#manufactured_ns_X = navier_stokes_X.subs([(velX, velX_expr), (velY, velY_expr)])
#manufactured_ns_Y = navier_stokes_Y.subs([(velX, velX_expr), (velY, velY_expr)])
#
#eqns = [navier_stokes_X, manufactured_ns_X, manufactured_ns_Y]


if __name__ == '__main__':
    for plot in plots:
        plot.show()

    # for eqn in eqns:
    #     print(eqn)
