def solve(N):
    
    # Write your code here
    binary_sum = 0
    while N > 0:
        binary_sum += N % 2
        N //= 2
    return binary_sum

if