import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2  # Example function, you can change this to any function

def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    integral = (y[0] + y[-1]) / 2 + np.sum(y[1:-1])
    return integral * dx

def plot_trapezoidal(f, a, b, n):
    x = np.linspace(a, b, 1000)
    y = f(x)
    
    x_trap = np.linspace(a, b, n+1)
    y_trap = f(x_trap)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label='Function')
    plt.fill_between(x_trap, 0, y_trap, alpha=0.3)
    
    for i in range(n):
        plt.plot([x_trap[i], x_trap[i]], [0, y_trap[i]], 'r--')
        plt.plot([x_trap[i], x_trap[i+1]], [y_trap[i], y_trap[i+1]], 'r-')
    plt.plot([x_trap[-1], x_trap[-1]], [0, y_trap[-1]], 'r--')
    
    plt.title(f'Trapezoidal Rule with {n} trapezoids')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
a, b = 0, 2  # Integration limits
n = 5  # Number of trapezoids

result = trapezoidal_rule(f, a, b, n)
print(f"Approximate integral using {n} trapezoids: {result}")

plot_trapezoidal(f, a, b, n)



# # Define the function to integrate
# def f(x):
#     return x**2

# # Define the limits of integration
# a = 0  # Lower limit
# b = 1  # Upper limit

# # Define the number of subintervals
# n = 4

# # Calculate the width of each subinterval
# h = (b - a) / n

# # Initialize the sum of trapezoidal areas
# area = 0

# # Iterate through the subintervals
# for i in range(n):
#     # Calculate the x values at the endpoints of the subinterval
#     x0 = a + i * h
#     x1 = a + (i + 1) * h

#     # Calculate the area of the trapezoid
#     area += (f(x0) + f(x1)) * h / 2

# # Print the result
# print("Approximate integral:", area)
