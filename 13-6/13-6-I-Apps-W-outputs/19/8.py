
def solve(n, cities):
    # Calculate the distance between each pair of cities
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            distance = abs(cities[i] - cities[j])
            distances.append(distance)
    
    # Find the minimum distance and the number of pairs with that distance
    min_distance = min(distances)
    num_pairs = 0
    for distance in distances:
        if distance == min_distance:
            num_pairs += 1
    
    return min_distance, num_pairs

