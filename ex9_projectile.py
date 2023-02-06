# import math would import the whole module
# inefficient, need to type math. before each function

# from math import <<function>> would just import the required function
# don't need to type math., more efficient unless you need to do a huge number of functions
# another option is from math import *
# * is a wildcard and means to import all functions, but you still don't need to type math.

# import required functions from math module
from math import pi
from math import tan
from math import cos

# acceleration due to gravity (m/s^2)
g = 9.81
# initial velocity (m/s)
v_0 = 44
# elevation angle
theta_deg = 80
theta_rad = (theta_deg*pi)/180
# horizontal distance travelled (m)
x = 0.5
# height of the barrel (m)
y_0 = 1

num = g * x ** 2
# print(num)

denom = 2 * (v_0 * cos(theta_rad)) ** 2

fraction = num / denom

# height of a projectile
projectileHeight = y_0 + x*tan(theta_rad) - fraction
print(projectileHeight)

