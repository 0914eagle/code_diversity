def starts_one_ends(n):
    
    count = 0
    for i in range(1, n + 1):
        if is_one(i):
            count += 1
    return count


