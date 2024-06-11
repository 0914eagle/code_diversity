def even_odd_palindrome(n):
    
    # initialize counter
    even, odd = 0, 0
    # loop through all numbers
    for i in range(1, n + 1):
        # convert number to string
        num = str(i)
        # check if number is palindrome
        if num == num[::-1]:
            # check if number is even
            if i % 2 == 0:
                even += 1
            # check if number is odd
            else:
                odd += 1
    return even, odd


