
def solve(n, x):
    # Calculate the maximum distance between any two points
    max_distance = max([abs(x[i] - x[j]) for i in range(n) for j in range(i+1, n)])
    
    # Calculate the sum of the maximum distance for all non-empty subsets
    sum = 0
    for i in range(1, 2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(j)
        if len(subset) > 1:
            sum += max_distance
    
    return sum % 1000000007

