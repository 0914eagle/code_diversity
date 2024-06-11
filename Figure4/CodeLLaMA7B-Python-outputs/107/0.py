def even_odd_palindrome(n):
    
    # initialize
    even, odd = 0, 0

    # loop through all numbers
    for i in range(1, n + 1):
        # convert to string
        s = str(i)

        # check if it is palindrome
        if s == s[::-1]:
            # check if it is even or odd
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

    return even, odd
