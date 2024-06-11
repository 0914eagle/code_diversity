def starts_one_ends(n):
    
    count = 0
    for i in range(1, n + 1):
        if str(i).startswith('1') and str(i).endswith('1'):
            count += 1
    return count


