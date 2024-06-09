
def solve(n, k, arr):
    # Sort the array to group similar integers together
    arr.sort()
    # Initialize the minimum number of balls to rewrite as 0
    min_balls = 0
    # Initialize the current group size as 1
    group_size = 1
    # Iterate through the array
    for i in range(n-1):
        # If the current integer is different from the previous integer, increment the group size
        if arr[i] != arr[i+1]:
            group_size += 1
        # If the group size is greater than the allowed group size, increment the minimum number of balls to rewrite
        if group_size > k:
            min_balls += 1
            group_size = 1
    # Return the minimum number of balls to rewrite
    return min_balls

