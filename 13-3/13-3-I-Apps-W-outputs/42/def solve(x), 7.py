
def solve(x):
    # Find the closest number to x that is a perfect cube
    # This is the number of rolls Mishka can make to get exactly x points
    cube_root = x**(1/3)
    return int(cube_root)

