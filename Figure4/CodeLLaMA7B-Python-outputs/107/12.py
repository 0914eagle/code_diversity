def even_odd_palindrome(n):
    
    # initialize variables
    even_palindromes = 0
    odd_palindromes = 0

    # loop through all numbers from 1 to n
    for i in range(1, n + 1):
        # if the number is a palindrome
        if str(i) == str(i)[::-1]:
            # if the number is even
            if i % 2 == 0:
                even_palindromes += 1
            # if the number is odd
            else:
                odd_palindromes += 1

    return (even_palindromes, odd_palindromes)
