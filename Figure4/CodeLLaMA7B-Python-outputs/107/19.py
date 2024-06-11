def even_odd_palindrome(n):
    
    # initialize the count of even and odd integer palindromes
    even_count, odd_count = 0, 0

    # loop over the range(1, n + 1)
    for i in range(1, n + 1):
        # convert the integer to string
        s = str(i)

        # if the integer is a palindrome
        if s == s[::-1]:
            # if the integer is even
            if i % 2 == 0:
                # increment the count of even integer palindromes
                even_count += 1
            # otherwise
            else:
                # increment the count of odd integer palindromes
                odd_count += 1

    # return the tuple of the count of even and odd integer palindromes
    return even_count, odd_count
