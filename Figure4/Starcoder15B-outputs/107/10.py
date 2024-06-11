def even_odd_palindrome(n):
    
    even, odd = 0, 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd

