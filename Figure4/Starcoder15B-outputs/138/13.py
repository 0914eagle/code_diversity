def is_equal_to_sum_even(n):
    
    # Your code here
    if n % 2 == 0:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    for l in range(1, n):
                        if i + j + k + l == n:
                            return True
    return False


