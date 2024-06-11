def starts_one_ends(n):
    
    # 10**(n-1) is the largest number that has n-1 digits
    # 10**n is the largest number that has n digits
    # 10**(n-1) < n < 10**n
    # 10**(n-1) + 10**(n-1) is the sum of all numbers with n-1 digits
    # 10**(n-1) + 10**(n-1) + 10**(n-1) is the sum of all numbers with n digits
    # 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) is the sum of all numbers
    # with n+1 digits
    # 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) + 10**(n-1) is the sum of
    # all numbers with n+2 digits
    # ...
    # 10**(n-1) + 10**(n-1) + 10**(n-1) + ... + 10**(n-1) is the sum of all
    # numbers with n digits
    # 10**(n-1) + 10**(n-1) + 10**(n-1) + ... + 10**(n-1) + 10**(n-1) is the
    # sum of all numbers with n+1 digits
    # ...
    # 10**(n-1) + 10**(n-1) + 10**(n-1) + ... + 10**(n-1) + 10**(n-1) + 10**(n-1)
    # is the sum of all numbers with n+n digits
    # 10**(n-1) + 10**(n-1) + 10**(n-1) + ... + 10**(n-1) + 10