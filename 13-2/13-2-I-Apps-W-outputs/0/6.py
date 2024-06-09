
def count_problem_sets(n, l, r, x, c):
    # Initialize variables
    total_difficulty = 0
    min_difficulty = 10**9
    max_difficulty = 0
    count = 0
    
    # Iterate through the problems
    for i in range(n):
        # Calculate the total difficulty of the problemset
        total_difficulty += c[i]
        
        # Calculate the minimum and maximum difficulty of the problemset
        if c[i] < min_difficulty:
            min_difficulty = c[i]
        if c[i] > max_difficulty:
            max_difficulty = c[i]
        
        # Check if the problemset is suitable
        if total_difficulty >= l and total_difficulty <= r and max_difficulty - min_difficulty >= x:
            count += 1
    
    return count

