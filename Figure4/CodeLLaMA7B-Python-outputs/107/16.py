def even_odd_palindrome(n):
    
    # initialize
    even, odd = 0, 0
    # loop over the range
    for i in range(1, n + 1):
        # check if the number is a palindrome
        if str(i) == str(i)[::-1]:
            # check if the number is even or odd
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)


