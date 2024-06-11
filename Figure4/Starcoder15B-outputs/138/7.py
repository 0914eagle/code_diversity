def is_equal_to_sum_even(n):
    
    # YOUR CODE HERE
    if n % 2 == 0:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    for l in range(1, n):
                        if i + j + k + l == n and i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                            return True
    return False


