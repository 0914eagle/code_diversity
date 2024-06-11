def is_equal_to_sum_even(n):
    
    return sum([i for i in range(1, n + 1) if i % 2 == 0 and i % 4 == 0]) == n


