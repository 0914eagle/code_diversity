
def solve(x):
    # Find the closest number to x that is a perfect square
    # This is the number of rolls Mishka can make to get exactly x points
    return int(round(x**0.5))**2

