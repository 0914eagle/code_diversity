
def solve(n, x, v):
    # Calculate the minimum distance between two points
    def min_distance(i, j):
        if v[i] == v[j]:
            return abs(x[i] - x[j])
        else:
            return abs(x[i] - x[j]) / abs(v[i] - v[j])
    
    # Calculate the sum of minimum distances over all pairs of points
    sum_distances = 0
    for i in range(n):
        for j in range(i+1, n):
            sum_distances += min_distance(i, j)
    
    return sum_distances

