def even_odd_palindrome(n):
    
    # initialize the count of even and odd palindromes
    even_count, odd_count = 0, 0

    # loop through all the numbers from 1 to n
    for i in range(1, n + 1):
        # convert the number to string
        num_str = str(i)

        # check if the number is palindrome
        if num_str == num_str[::-1]:
            # check if the number is even or odd
            if i % 2 == 0:
                # increment the count of even palindromes
                even_count += 1
            else:
                # increment the count of odd palindromes
                odd_count += 1

    # return the count of even and odd palindromes
    return even_count, odd_count
