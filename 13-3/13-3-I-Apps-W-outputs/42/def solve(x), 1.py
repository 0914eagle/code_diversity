
def solve(x):
    # Find the closest number to x that is a perfect cube
    cube_root = x**(1/3)
    closest_cube = int(cube_root + 1) ** 3

    # Return the number of rolls needed to get closest_cube points
    return int(closest_cube / x)

