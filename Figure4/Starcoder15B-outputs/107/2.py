def even_odd_palindrome(n):
    
    if n < 1:
        return (0, 0)

    even = 0
    odd = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

    return (even, odd)

