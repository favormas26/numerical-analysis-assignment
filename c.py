import numpy as np
import scipy as sp

x = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# linear spline function
f = sp.interpolate.interp1d(x, y, kind='linear')

x_new = 4.0
y_new = f(x_new)

print("Value of y at x =", x_new, "is", y_new)
