def starts_one_ends(n):
    
    # 10**(n-1) is the largest number that has n-1 digits
    # 10**n is the smallest number that has n digits
    # 10**(n-1) + 10**n is the range of numbers that has n digits
    # 10**(n-1) + 10**n - 10**(n-1) is the range of numbers that has n digits
    # - 10**(n-1) is the range of numbers that has n digits minus the range of
    # numbers that has n-1 digits
    # 10**(n-1) + 10**n - 10**(n-1) - 10**(n-1) is the range of numbers that
    # has n digits minus the range of numbers that has n-1 digits minus the
    # range of numbers that has n-2 digits
    # 10**(n-1) + 10**n - 10**(n-1) - 10**(n-1) - 10**(n-2) is the range of
    # numbers that has n digits minus the range of numbers that has n-1 digits
    # minus the range of numbers that has n-2 digits minus the range of numbers
    # that has n-3 digits
    # ...
    # 10**(n-1) + 10**n - 10**(n-1) - 10**(n-1) - ... - 10**(n-n) is the range
    # of numbers that has n digits minus the range of numbers that has n-1
    # digits minus the range of numbers that has n-2 digits minus the range of
    # numbers that has n-3 digits minus ... minus the range of numbers that has
    # n-n digits
    # 10**(n-1) + 10**n - 10**(n-1) - 10**(n-1) - ... - 10**(n-n) + 10**(n-n)
    # is the range of numbers that has n digits minus the range of numbers that
