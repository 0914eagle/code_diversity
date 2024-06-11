def starts_one_ends(n):
    
    return sum(1 for i in range(1, n) if i % 10 == 1 or i % 10 == 9)


