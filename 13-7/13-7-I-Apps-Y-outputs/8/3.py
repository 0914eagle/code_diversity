
def solve(n, k, arr):
    # Sort the array to group similar elements together
    arr.sort()
    # Initialize the minimum number of balls to rewrite as 0
    min_balls = 0
    # Initialize the current group size as 1
    group_size = 1
    # Iterate through the array
    for i in range(n-1):
        # If the current element is different from the next element, we need to rewrite the integers on the current group
        if arr[i] != arr[i+1]:
            # Increment the minimum number of balls
            min_balls += 1
            # Reset the group size
            group_size = 1
        # If the group size is greater than or equal to the maximum number of different integers allowed, we need to rewrite the integers on the current group
        elif group_size >= k:
            # Increment the minimum number of balls
            min_balls += 1
            # Reset the group size
            group_size = 1
        # Otherwise, increment the group size
        else:
            group_size += 1
    # Return the minimum number of balls needed to rewrite the integers on them
    return min_balls

