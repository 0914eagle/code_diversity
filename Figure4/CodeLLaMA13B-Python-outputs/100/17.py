def make_a_pile(n):
    
    result = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else (n + 1) // 2
        result.append(n)
    return result


