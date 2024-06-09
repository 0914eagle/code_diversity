
def solve(balls, k):
    # Sort the balls in non-decreasing order
    balls.sort()
    # Initialize the number of different integers to 1
    num_different = 1
    # Initialize the number of balls to rewrite to 0
    num_rewrite = 0
    # Iterate through the balls
    for i in range(len(balls)):
        # If the current ball has a different integer than the previous ball
        if i == 0 or balls[i] != balls[i-1]:
            # Increment the number of different integers
            num_different += 1
        # If the number of different integers is greater than the maximum allowed
        if num_different > k:
            # Increment the number of balls to rewrite
            num_rewrite += 1
            # Reset the number of different integers to 1
            num_different = 1
    # Return the number of balls to rewrite
    return num_rewrite

