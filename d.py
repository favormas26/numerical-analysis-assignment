def newton_raphson(f, g, x0, tolerance=1e-12, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            return x
        fpx = g(x)
        if fpx == 0:
            return None  # Avoid division by zero
        x = x - fx / fpx
        
        # absolute relative approximation error
        ea = abs((x - x0) / x) * 100
        x0 = x
        print(i, ea, x, fx)
        
    return None  # Max iterations reached without convergence

# Define our function and its derivative
def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

def g(x):
    return 3*x**2  - 0.33*x

root = newton_raphson(f, g, 0.05, max_iterations=10)

if root is not None:
    print(f"The depth is approximately {root:.6f}m")
else:
    print("Failed to converge")