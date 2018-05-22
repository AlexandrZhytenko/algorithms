# numerical_integration
# y = 1 + x + sin2x

def f(x):
    import math
    return 1 + x + math.sin(2 * x)

def show_function_f_x(xmin=0, xmax=5.0):
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.arange(xmin, xmax, 0.1)
    y = np.vectorize(f)
    plt.title("y = 1 + x + sin2x")
    plt.axis([0, 5, 0, 7])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.tight_layout()
    plt.text(2, 1, "Have to find this square!")
    plt.plot(x, y(x), "r", linewidth=3)
    plt.fill_between(x, y(x), color="grey")
    plt.show()

def rectangle_rule(xmin=0.0, xmax=5.0, intervals=10):
    dx = (xmax - xmin) / intervals
    total_area = 0
    x = xmin
    for i in range(intervals):
        total_area += dx * f(x)
        x = x + dx
    return round(total_area, 2)

# TrapezoidRule
def trapezoid_rule(xmin=0.0, xmax=5.0, intervals=10):
    dx = (xmax - xmin) / intervals
    total_area = 0
    x = xmin
    for i in range(intervals):
        total_area += dx * (f(x) + f(x + dx)) / 2
        x = x + dx
    return round(total_area, 2)

# Adaptive Midpoint Integration
def adaptive_midpoint_integration(xmin=0.0,
                                  xmax=5.0,
                                  intervals=10,
                                  max_slice_error=.01):
    dx = (xmax - xmin) / intervals
    total_area = 0
    x = xmin
    for i in range(intervals):
        total_area += slice_area(x, x + dx, max_slice_error)
        x = x + dx
    return round(total_area, 2)

def slice_area(x1, x2, max_slice_error):
    y1 = f(x1)
    y2 = f(x2)
    xm = (x1 + x2) / 2
    ym = f(xm)
    area12 = (x2 - x1) * (y1 + y2) / 2.0
    area1m = (xm - x1) * (y1 + ym) / 2.0
    aream2 = (x2 - xm) * (ym + y2) / 2.0
    area1m2 = area1m + aream2
    error = (area1m2 - area12) / area12
    if abs(error) < max_slice_error:
        return area1m2
    return slice_area(x1, xm, max_slice_error) + \
slice_area(xm, x2, max_slice_error)

if __name__ == "__main__":
    print "result for rectangle_rule = {}".format(rectangle_rule())
    print "result for trapezoid_rule = {}".format(trapezoid_rule())
    print "result for daptive_midpoint_integration = {}".format(adaptive_midpoint_integration())
    show_function_f_x()