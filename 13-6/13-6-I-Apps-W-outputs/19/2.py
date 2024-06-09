
def solve(n, a):
    # Calculate the distance between each pair of cities
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            distance = abs(a[i] - a[j])
            distances.append(distance)
    
    # Find the minimum distance and its count
    min_distance = min(distances)
    count = distances.count(min_distance)
    
    return min_distance, count

