
def f1(n, k, d, s):
    # Calculate the average difficulty of the solved problems
    avg_solved = s * k / n
    
    # Calculate the average difficulty of the unsolved problems
    avg_unsolved = (d - avg_solved) * (n - k) / n
    
    # Check if the average difficulty of the unsolved problems is possible
    if avg_unsolved < 0 or avg_unsolved > 100:
        return "impossible"
    
    # Return the average difficulty of the unsolved problems
    return avg_unsolved
