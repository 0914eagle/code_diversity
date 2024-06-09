
def solve(n, k, arr):
    # Sort the array in ascending order
    arr.sort()
    # Initialize a variable to store the minimum number of balls to be rewritten
    min_balls = 0
    # Initialize a variable to store the current number of different integers
    curr_diff = 1
    # Iterate through the array
    for i in range(n):
        # If the current integer is different from the previous integer, increment the current number of different integers
        if i == 0 or arr[i] != arr[i-1]:
            curr_diff += 1
        # If the current number of different integers is greater than the allowed number of different integers, increment the minimum number of balls to be rewritten
        if curr_diff > k:
            min_balls += 1
            curr_diff = 1
    # Return the minimum number of balls to be rewritten
    return min_balls

