def starts_one_ends(n):
    
    # 10^(n-1) + 10^(n-2) + ... + 10^2 + 10^1 + 10^0 = 10^n - 1
    return (10**n - 1) // 9


