def sum_to_n(n: int):
    
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)


