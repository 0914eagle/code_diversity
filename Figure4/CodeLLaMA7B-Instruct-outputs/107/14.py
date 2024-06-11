

def even_odd_palindrome(n):
    
    even_count = 0
    odd_count = 0

    for i in range(1, n+1):
        if is_palindrome(i) and i % 2 == 0:
            even_count += 1
        elif is_palindrome(i) and i % 2 == 1:
            odd_count += 1

    return (even_count, odd_count)

def
