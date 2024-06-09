
def hacked_computers(n, x):
    # Calculate the maximum distance between any two hacked computers
    max_distance = max([abs(x[i] - x[j]) for i in range(n) for j in range(i+1, n)])
    
    # Calculate the sum of the maximum distance for all non-empty subsets of hacked computers
    sum_subsets = 0
    for i in range(1, 2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(j)
        if len(subset) > 1:
            sum_subsets += max_distance
    
    return sum_subsets % 1000000007

