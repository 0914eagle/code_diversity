def is_equal_to_sum_even(n):
    
    if n % 2 == 0:
        for i in range(2, n, 2):
            for j in range(2, n, 2):
                for k in range(2, n, 2):
                    for l in range(2, n, 2):
                        if i + j + k + l == n:
                            return True
    return False


