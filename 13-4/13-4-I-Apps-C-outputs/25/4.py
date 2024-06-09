
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_distance = max(x[i] - x[i-1] for i in range(1, n))
    
    # Calculate the sum of F(a) for all non-empty subsets of computers
    sum = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            sum += max(x[j-1] - x[i-1], max_distance - (x[j-1] - x[i-1]))
    
    return sum % 1000000007

