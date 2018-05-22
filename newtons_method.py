# Newtons method
# is a method for finding successively better approximations
# to the roots (or zeroes) of a real valued function
# "y = x^3 / 5 - x^2 + x"

def f(x):
    return (x**3 / 5) - (x ** 2) + x

def show_function_f_x(xmin=-5, xmax=5.0):
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.arange(xmin, xmax, 0.1)
    y = np.vectorize(f)
    plt.title("y = x^3 / 5 - x^2 + x")
    plt.axis([-1, 5, -1, 5])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.tight_layout()
    plt.plot(x, y(x), "r", linewidth=3)
    plt.show()

def dfdx_show():
    from sympy import diff, symbols
    x = symbols("x")
    print diff((x**3 / 5) - (x ** 2) + x)

def dfdx(x):
    return (3*(x**2)/5) - 2*x + 1

def newtons_method(initial_guess=0):
    x = initial_guess
    while abs(f(x)) > 0.01:
        x -= float(f(x))/dfdx(x)
    return round(x, 2)

if __name__ == "__main__":
    for i in [-1, 2, 9]:
        print "The root is: ", newtons_method(i)
    show_function_f_x()