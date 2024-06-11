def solve(N):
    
    # 1. Check the input
    if N < 0 or N > 10000:
        raise ValueError('N must be between 0 and 10000')
    
    # 2. Solve the problem
    result = 0
    while N > 0:
        result += N % 2
        N //= 2
    
    # 3. Return the result
    return result


# Test