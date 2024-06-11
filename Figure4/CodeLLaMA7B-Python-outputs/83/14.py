def starts_one_ends(n):
    
    # 10**(n-1) is the largest number that has n-1 digits
    # 10**n is the largest number that has n digits
    # 10**(n-1) + 10**n is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) + 1 is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) + 10**(n-1) is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) + 10**(n-1) + 10**(n-1) is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) is the count of numbers that have n-1 or n digits
    # 10**(n-1) - 10**(n-1) + 10**(n-1) + 10**(n-1) + 1