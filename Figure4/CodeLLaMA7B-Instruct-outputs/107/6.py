

def even_odd_palindrome(n):
    
    even_count = 0
    odd_count = 0

    # Iterate through the range of palindromes
    for i in range(1, n+1):
        # Check if the number is a palindrome
        if str(i) == str(i)[::-1]:
            # Check if the number is even
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)

