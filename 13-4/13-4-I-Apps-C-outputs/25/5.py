
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_distance = max([abs(x[i] - x[j]) for i in range(n) for j in range(i+1, n)])
    
    # Calculate the sum of F(a) for all non-empty subsets of computers
    sum_F = 0
    for i in range(1, n+1):
        for subset in combinations(range(n), i):
            sum_F += max([abs(x[subset[j]] - x[subset[j+1]]) for j in range(len(subset)-1)])
    
    return sum_F % 1000000007

