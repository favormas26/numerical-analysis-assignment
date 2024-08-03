import numpy as np

def lagrange_interpolation(x, y):
    n = len(x)
    
    def L(i, x_val):
        numerator = np.prod([x_val - x[j] for j in range(n) if j != i])
        denominator = np.prod([x[i] - x[j] for j in range(n) if j != i])
        return numerator / denominator
    
    def P(x_val):
        return sum(y[i] * L(i, x_val) for i in range(n))
    
    # Generate coefficients
    x_poly = np.linspace(min(x), max(x), 100)
    y_poly = [P(xi) for xi in x_poly]
    
    coeffs = np.polyfit(x_poly, y_poly, n-1)
    return coeffs[::-1]  # Reverse to match standard polynomial notation

# Test the function
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
lagrange_coeffs = lagrange_interpolation(x, y)
print("Lagrange Coefficients:", lagrange_coeffs)

def newton_divided_difference(x, y):
    n = len(x)
    coeffs = [y[0]]
    
    for j in range(1, n):
        divided_diff = [0] * (n - j)
        for i in range(n - j):
            divided_diff[i] = (y[i+1] - y[i]) / (x[i+j] - x[i])
        y = divided_diff
        coeffs.append(y[0])
    
    return coeffs

# Test the function
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
newton_coeffs = newton_divided_difference(x, y)
print("Newton's Divided Difference Coefficients:", newton_coeffs)

import matplotlib.pyplot as plt

def evaluate_polynomial(coeffs, x):
    return sum(coeff * x**i for i, coeff in enumerate(coeffs))

# Given data points
x_data = [1, 2, 3, 4]
y_data = [1, 4, 9, 16]

# Lagrange interpolation
lagrange_coeffs = lagrange_interpolation(x_data, y_data)

# Newton's Divided Difference
newton_coeffs = newton_divided_difference(x_data, y_data)

# Generate points for plotting
x_plot = np.linspace(min(x_data), max(x_data), 100)
y_lagrange = [evaluate_polynomial(lagrange_coeffs, x) for x in x_plot]
y_newton = [sum(newton_coeffs[i] * np.prod([x - x_data[j] for j in range(i)]) for i in range(len(newton_coeffs))) for x in x_plot]

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='red', label='Data points')
plt.plot(x_plot, y_lagrange, label='Lagrange Interpolation')
plt.plot(x_plot, y_newton, '--', label="Newton's Divided Difference")
plt.legend()
plt.title('Polynomial Interpolation Comparison')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

print("Lagrange Coefficients:", lagrange_coeffs)
print("Newton's Coefficients:", newton_coeffs)