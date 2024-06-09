
def solve(K, N):
    # Calculate the number of combinations for each i
    combinations = [0] * (2 * K)
    for i in range(1, 2 * K + 1):
        combinations[i - 1] = combinations_sum(K, N, i)
    
    # Return the results modulo 998244353
    return [combination % 998244353 for combination in combinations]

# Calculate the number of combinations for a given i
def combinations_sum(K, N, i):
    # Base case: if N is 0, there are 0 combinations
    if N == 0:
        return 0
    
    # Base case: if N is 1, there is 1 combination if i is 1, and 0 otherwise
    if N == 1:
        if i == 1:
            return 1
        else:
            return 0
    
    # Recursive case: calculate the number of combinations for N-1 dice and i-1, i, i+1
    return combinations_sum(K, N-1, i-1) + combinations_sum(K, N-1, i) + combinations_sum(K, N-1, i+1)

