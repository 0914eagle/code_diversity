def is_equal_to_sum_even(n):
    
    if n % 2 == 1:
        return False
    else:
        for i in range(1, n):
            for j in range(i, n):
                for k in range(j, n):
                    for l in range(k, n):
                        if i + j + k + l == n:
                            return True
        return False


