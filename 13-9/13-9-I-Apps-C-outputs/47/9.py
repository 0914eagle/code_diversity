
def solve(a, b):
    # Find the minimum positive value of x such that the polyline passes through (a, b)
    # The polyline is defined by the points (0, 0) - (x, x) - (2x, 0) - (3x, x) - (4x, 0) - ... - (2kx, 0) - (2kx + x, x) - ...
    # We can write the equation of the polyline as:
    # f(x) = (x^2 - a)^2 + (x - b)^2
    # To find the minimum value of x, we can differentiate f(x) and set it to 0:
    # f'(x) = 2x(x - a) - 2(x - b)
    # We can then solve for x:
    x = (a + b)/2
    # Check if the polyline passes through (a, b)
    if (x**2 - a)**2 + (x - b)**2 == 0:
        return x
    else:
        return -1

