import numpy as np
import scipy as sp

# Differentiation - process of finding the derivative of a function

dx = np.array([1, 2, 3, 4, 5])
dy = np.array([2, 4, 6, 8, 10])

dy_dx = np.gradient(dy, dx)
print(dy_dx)

# Numerical integration - process of finding the definite integral of a function

nx = np.array([0, 1, 2, 3, 4, 5])
ny = np.array([0, 1, 4, 9, 16, 25])

ny_int = sp.integrate.simpson(y=ny, x=nx)
print(ny_int)

# Curve fitting - process of finding a curve that best fits a given set of data points

def curve(x, a, b, c):
    return a * np.exp(-b * x) + c

cx = np.array([0, 1, 2, 3, 4, 5])
cy = np.array([2.1, 1.1, 0.6, 0.3, 0.1, 0.05])

params, _ = sp.optimize.curve_fit(curve, cx, cy)
print(params)

# Linear Regression - process of finding the best-fitting straight line through a set of data points

lx = np.array([0, 1, 2, 3, 4, 5])
ly = np.array([1, 3, 5, 7, 9, 11])

slope, intercept = np.polyfit(lx, ly, 1)
print(slope, intercept)

# Spline interpolation - process of constructing a smooth curve that passes through a given set of data points

sx = np.array([0, 1, 2, 3, 4, 5])
sy = np.array([0, 1, 4, 9, 16, 25])

spline = sp.interpolate.splrep(sx, sy)

new_sx = np.linspace(0, 5, 100)
new_sy = sp.interpolate.splev(new_sx, spline)
print(new_sy)