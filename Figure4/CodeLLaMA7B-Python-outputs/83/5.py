def starts_one_ends(n):
    
    # 10**(n-1) is the largest number that has n-1 digits
    # 10**(n-1) + 10**(n-1) - 1 is the largest number that has n digits
    return (10**(n-1) + 10**(n-1) - 1) - (10**(n-1) - 1)


