
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum number of balls to rewrite as 0
    min_balls = 0
    # Initialize the current number of different integers as 1
    current_ints = 1
    # Iterate through the array
    for i in range(n):
        # If the current integer is different from the previous integer, increment the current number of different integers
        if i == 0 or arr[i] != arr[i-1]:
            current_ints += 1
        # If the current number of different integers is greater than the allowed number of different integers, increment the minimum number of balls to rewrite
        if current_ints > k:
            min_balls += 1
            current_ints = 1
    # Return the minimum number of balls to rewrite
    return min_balls

