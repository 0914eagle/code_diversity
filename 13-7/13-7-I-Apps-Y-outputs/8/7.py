
def solve(n, k, arr):
    # Sort the array to group similar elements together
    arr.sort()
    # Initialize a variable to store the minimum number of balls to be rewritten
    min_balls = 0
    # Initialize a variable to store the current group size
    group_size = 1
    # Iterate over the array
    for i in range(n-1):
        # If the current element is not equal to the next element, it means we have found the end of a group
        if arr[i] != arr[i+1]:
            # If the group size is greater than the maximum number of groups allowed, we need to rewrite the integers on these balls
            if group_size > k:
                min_balls += group_size - k
            # Reset the group size
            group_size = 1
        else:
            # Increment the group size
            group_size += 1
    # Check if the last group needs to be rewritten
    if group_size > k:
        min_balls += group_size - k
    return min_balls

