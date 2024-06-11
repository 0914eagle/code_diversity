def even_odd_palindrome(n):
    
    even, odd = 0, 0
    for i in range(1, n+1):
        j = int(str(i)[::-1])
        if i == j:
            even += 1
        else:
            odd += 1
    return even, odd
