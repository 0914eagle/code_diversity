def starts_one_ends(n):
    
    # 10**(n-1) is the largest number that has n-1 digits
    # 10**n is the largest number that has n digits
    # 10**n - 10**(n-1) is the difference between the two
    # 10**n - 10**(n-1) + 1 is the largest number that has n digits and ends with 1
    # 10**n - 10**(n-1) + 1 - 10**n is the difference between the two
    # 10**n - 10**(n-1) + 1 - 10**n + 1 is the largest number that has n digits and starts with 1
    # 10**n - 10**(n-1) + 1 - 10**n + 1 - 10**n is the difference between the two
    # 10**n - 10**(n-1) + 1 - 10**n + 1 - 10**n + 1 is the largest number that has n digits and starts with 1 and ends with 1
    # 10**n - 10**(n-1) + 1 - 10**n + 1 - 10**n + 1 - 10**n is the difference between the two
    # 10**n - 10**(n-1) + 1 - 10**n + 1 - 10**n + 1 - 10**n + 1 is the largest number that has n digits and starts with 1 and ends with 1
    # 10**n - 10**(n-1) + 1 - 10**n + 1 - 10**n + 1 - 10**n + 1 - 10**n is the difference between the two
    # 10**n - 10**(n-1) + 1 - 10**n + 1 - 10**n + 1 - 10**n + 1 - 10**n + 1 is the largest number that has n