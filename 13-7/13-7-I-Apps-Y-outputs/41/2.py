
def max_removable_cubes(S):
    # Initialize variables to keep track of the number of red and blue cubes
    num_red_cubes, num_blue_cubes = 0, 0
    
    # Iterate through the string S
    for cube in S:
        if cube == "0":
            num_red_cubes += 1
        else:
            num_blue_cubes += 1
    
    # The maximum number of cubes that can be removed is the minimum of the number of red and blue cubes
    return min(num_red_cubes, num_blue_cubes)

