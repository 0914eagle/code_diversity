
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_distance = max([abs(x[i] - x[j]) for i in range(n) for j in range(i+1, n)])
    
    # Calculate the sum of the maximum distances for all non-empty subsets
    sum = 0
    for i in range(1, n+1):
        for subset in combinations(range(n), i):
            sum += max_distance
    
    return sum % 1000000007
