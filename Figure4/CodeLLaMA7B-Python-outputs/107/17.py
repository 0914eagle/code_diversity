def even_odd_palindrome(n):
    
    # initialize
    even, odd = 0, 0
    # loop over all numbers in range(1, n)
    for i in range(1, n+1):
        # convert number to string
        s = str(i)
        # check if number is palindrome
        if s == s[::-1]:
            # check if number is even or odd
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd


