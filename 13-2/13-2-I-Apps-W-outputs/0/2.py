
def count_problem_sets(n, l, r, x, c):
    # Initialize variables
    total_difficulty = 0
    min_difficulty = 10**6
    max_difficulty = 0
    count = 0
    
    # Iterate through the problems
    for i in range(n):
        # Calculate the total difficulty of the problems
        total_difficulty += c[i]
        # Find the minimum and maximum difficulty of the problems
        if c[i] < min_difficulty:
            min_difficulty = c[i]
        if c[i] > max_difficulty:
            max_difficulty = c[i]
    
    # Check if the total difficulty is within the required range
    if l <= total_difficulty <= r:
        # Check if the difference in difficulty is within the required range
        if max_difficulty - min_difficulty >= x:
            count += 1
    
    return count

