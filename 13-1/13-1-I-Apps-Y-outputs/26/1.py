
def solve(n, x, v):
    # Calculate the minimum distance between two points
    def min_dist(i, j):
        if v[i] == v[j]:
            return abs(x[i] - x[j])
        else:
            return abs(x[i] - x[j]) / abs(v[i] - v[j])
    
    # Calculate the sum of minimum distances over all pairs of points
    sum_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            sum_dist += min_dist(i, j)
    
    return sum_dist

