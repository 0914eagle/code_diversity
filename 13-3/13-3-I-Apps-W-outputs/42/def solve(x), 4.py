
def solve(x):
    # Find the closest number to x that is a perfect cube
    cube_root = x**(1/3)
    closest_cube = int(cube_root)
    if cube_root - closest_cube > 0.5:
        closest_cube += 1
    return closest_cube

