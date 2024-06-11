def starts_one_ends(n):
    
    if n == 1:
        return 1
    return 9 * starts_one_ends(n - 1) + 10 ** (n - 1)


