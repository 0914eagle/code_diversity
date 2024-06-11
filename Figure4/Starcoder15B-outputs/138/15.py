def is_equal_to_sum_even(n):
    
    if n % 2 != 0:
        return False
    if n == 8:
        return True
    for i in range(2, n // 2 + 1, 2):
        for j in range(i, n // 2 + 1, 2):
            for k in range(j, n // 2 + 1, 2):
                for l in range(k, n // 2 + 1, 2):
                    if i + j + k + l == n:
                        return True
    return False


