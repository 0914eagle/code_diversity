def is_equal_to_sum_even(n):
    
    if n % 2 == 1:
        return False
    else:
        for i in range(2, n):
            for j in range(2, n):
                for k in range(2, n):
                    for l in range(2, n):
                        if i + j + k + l == n:
                            return True
    return False


