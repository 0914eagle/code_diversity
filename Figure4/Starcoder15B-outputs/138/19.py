def is_equal_to_sum_even(n):
    
    if n < 8:
        return False
    for i in range(2, n // 2):
        for j in range(i + 1, n // 2):
            for k in range(j + 1, n // 2):
                for l in range(k + 1, n // 2):
                    if i + j + k + l == n:
                        return True
    return False


