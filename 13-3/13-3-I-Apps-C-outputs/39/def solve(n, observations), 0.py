
def solve(n, observations):
    # Initialize the number of ways to assign costumes as 1
    num_ways = 1

    # Iterate over each observation
    for observation in observations:
        # Get the number of children to the left and right of the current child
        l, r, x = observation

        # If the current child is wearing the orange pumpkin costume, update the number of ways to assign costumes
        if x == 1:
            num_ways *= (l + r) % 1000000007
        # If the current child is wearing the black bat costume, update the number of ways to assign costumes
        else:
            num_ways *= (l * r) % 1000000007

    # Return the number of ways to assign costumes
    return num_ways

