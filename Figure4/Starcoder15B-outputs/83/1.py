def starts_one_ends(n):
    
    if n == 1:
        return 10
    if n == 2:
        return 18
    return 9 * starts_one_ends(n - 1)


