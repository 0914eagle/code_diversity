def starts_one_ends(n):
    
    if n == 1:
        return 2
    return 10 * starts_one_ends(n - 1)


