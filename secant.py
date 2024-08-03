def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    """
    Secant method for finding the root of a function f.
    
    Parameters:
    f (function): The function for which we want to find the root.
    x0 (float): The first initial guess.
    x1 (float): The second initial guess.
    tol (float): The tolerance for the root value. Defaults to 1e-5.
    max_iter (int): The maximum number of iterations. Defaults to 100.
    
    Returns:
    float: The estimated root of the function.
    """
    for _ in range(max_iter):
        if abs(x1 - x0) < tol:
            return x1
        try:
            # Calculate the new approximation for the root
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        except ZeroDivisionError:
            print("Error: Division by zero encountered in secant method.")
            return None
        
        # Update the guesses
        x0, x1 = x1, x2
        
        # Check for convergence
        if abs(f(x1)) < tol:
            return x1
    
    print("Warning: Secant method did not converge within the maximum number of iterations.")
    return x1

if __name__ == "__main__":
    # Get user input for the function, initial guesses, and other parameters
    from sympy import sympify, lambdify
    import numpy as np
    
    # Input the function as a string
    func_str = input("Enter the function f(x): ")
    
    # Convert the string to a sympy expression
    f_sympy = sympify(func_str)
    
    # Convert the sympy expression to a Python function
    f = lambdify('x', f_sympy, 'numpy')
    
    # Get the initial guesses from the user
    x0 = float(input("Enter the first initial guess x0: "))
    x1 = float(input("Enter the second initial guess x1: "))
    
    # Optional: get the tolerance and max iterations from the user
    tol = float(input("Enter the tolerance (default is 1e-5): ") or 1e-5)
    max_iter = int(input("Enter the maximum number of iterations (default is 100): ") or 100)
    
    # Find the root using the secant method
    root = secant_method(f, x0, x1, tol, max_iter)
    
    if root is not None:
        print(f"The root found is: {root}")
