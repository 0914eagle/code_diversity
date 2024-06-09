
def solve(n, planets):
    # Initialize the distance matrix with the Euclidean distance between each pair of planets
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distance_matrix[i][j] = distance_matrix[j][i] = ((planets[i][0] - planets[j][0]) ** 2 + (planets[i][1] - planets[j][1]) ** 2 + (planets[i][2] - planets[j][2]) ** 2) ** 0.5
    
    # Initialize the visited matrix with all False values
    visited = [[False] * n for _ in range(n)]
    
    # Initialize the distance variable to 0
    distance = 0
    
    # Initialize the current planet index to 0
    current_planet = 0
    
    # Loop until all planets have been visited
    while not all(all(row) for row in visited):
        # Find the next planet to visit by finding the planet with the minimum distance from the current planet that has not been visited yet
        next_planet = 0
        min_distance = float('inf')
        for i in range(n):
            if not visited[current_planet][i] and distance_matrix[current_planet][i] < min_distance:
                min_distance = distance_matrix[current_planet][i]
                next_planet = i
        
        # Update the distance and visited matrix
        distance += min_distance
        visited[current_planet][next_planet] = visited[next_planet][current_planet] = True
        current_planet = next_planet
    
    # Return the total distance traveled
    return distance

