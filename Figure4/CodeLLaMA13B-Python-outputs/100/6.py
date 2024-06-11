def make_a_pile(n):
    
    result = []
    while n > 0:
        result.append(n)
        n = n + 1 if n % 2 else n - 1
    return result


