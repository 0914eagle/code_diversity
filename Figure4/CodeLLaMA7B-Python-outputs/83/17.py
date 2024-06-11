def starts_one_ends(n):
    
    # We can use the formula for the sum of the first n natural numbers
    # to count the number of n-digit positive integers that start or end
    # with 1.
    return n * (n + 1) // 2


