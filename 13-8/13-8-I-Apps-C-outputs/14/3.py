
def solve(K, N):
    # Calculate the number of combinations for each i
    combinations = [0] * (2 * K)
    for i in range(1, 2 * K + 1):
        combinations[i - 1] = combinations_sum(i, N, K)
    
    # Return the combinations modulo 998244353
    return [combination % 998244353 for combination in combinations]

def combinations_sum(i, N, K):
    # Base case: if N is 0, there are no combinations
    if N == 0:
        return 0
    
    # Base case: if N is 1, there is only one combination (i)
    if N == 1:
        return 1
    
    # Recursive case: calculate the number of combinations for i-1 and i-K
    return combinations_sum(i - 1, N - 1, K) + combinations_sum(i - K, N - 1, K)

