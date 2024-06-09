
def solve(n, a):
    # Calculate the distance between each pair of cities
    distances = [(abs(a[i] - a[j]), i, j) for i in range(n) for j in range(i+1, n)]
    
    # Sort the distances in ascending order
    distances.sort()
    
    # Initialize the minimum distance and quantity of pairs with this distance
    min_distance = distances[0][0]
    quantity = 1
    
    # Iterate through the distances and count the quantity of pairs with the same distance as the minimum distance
    for distance in distances:
        if distance[0] == min_distance:
            quantity += 1
    
    return min_distance, quantity

