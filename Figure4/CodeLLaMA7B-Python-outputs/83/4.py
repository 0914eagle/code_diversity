def starts_one_ends(n):
    
    # 10**(n-1) is the largest number that can be formed with n-1 digits
    # 10**n is the largest number that can be formed with n digits
    # 10**(n-1) + 10**n is the sum of all numbers that can be formed with n-1
    # and n digits
    # 10**(n-1) - 10**(n-1) + 1 is the count of numbers that start with 1
    # 10**(n-1) - 10**(n-1) + 10 is the count of numbers that end with 1
    # 2 * (10**(n-1) - 10**(n-1) + 1) is the count of numbers that start or end
    # with 1
    return 2 * (10**(n-1) - 10**(n-1) + 1)


