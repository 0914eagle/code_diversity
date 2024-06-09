
def max_cubes_removed(S):
    # Initialize variables
    N = len(S)
    red_cubes = 0
    blue_cubes = 0
    max_removed = 0

    # Iterate through the string
    for i in range(N):
        if S[i] == "0":
            red_cubes += 1
        else:
            blue_cubes += 1

        # If both the current cube and the next cube are the same color, remove them
        if i < N-1 and S[i] == S[i+1]:
            if S[i] == "0":
                red_cubes -= 2
            else:
                blue_cubes -= 2
            max_removed += 2

    # Return the maximum number of cubes that can be removed
    return max(red_cubes, blue_cubes)

