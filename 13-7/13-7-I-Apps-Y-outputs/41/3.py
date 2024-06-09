
def max_cubes_removed(S):
    # Initialize variables to keep track of red and blue cubes
    red_cubes, blue_cubes = 0, 0
    
    # Iterate through the string S
    for cube in S:
        if cube == "0":
            red_cubes += 1
        else:
            blue_cubes += 1
    
    # The maximum number of cubes that can be removed is the minimum of the number of red and blue cubes
    return min(red_cubes, blue_cubes)

