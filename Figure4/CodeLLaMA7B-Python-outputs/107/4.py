def even_odd_palindrome(n):
    
    # initialize the result
    even, odd = 0, 0

    # loop for all the numbers in the range
    for i in range(1, n + 1):
        # convert the number to string
        s = str(i)

        # check if the number is palindrome
        if s == s[::-1]:
            # check if the number is even or odd
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

    return even, odd
