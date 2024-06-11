def starts_one_ends(n):
    
    if n < 10:
        return 0
    count = 0
    for i in range(1, 10):
        if n % i == 0:
            count += 1
    return count


