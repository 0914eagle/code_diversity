
def solve(n, planets):
    # Initialize the distance matrix with the Euclidean distance between each pair of planets
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist_matrix[i][j] = dist_matrix[j][i] = ((planets[i][0]-planets[j][0])**2 + (planets[i][1]-planets[j][1])**2 + (planets[i][2]-planets[j][2])**2)**0.5
    
    # Initialize the visited matrix with all planets set to False
    visited = [False] * n
    
    # Initialize the total distance traveled to 0
    total_dist = 0
    
    # Start at the home planet
    current_planet = 0
    visited[current_planet] = True
    
    # Loop until all planets have been visited
    while True:
        # Find the next planet to visit
        next_planet = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist_matrix[current_planet][i] < min_dist:
                min_dist = dist_matrix[current_planet][i]
                next_planet = i
        if next_planet == -1:
            break
        
        # Visit the next planet
        visited[next_planet] = True
        total_dist += dist_matrix[current_planet][next_planet]
        current_planet = next_planet
    
    # Return the total distance traveled
    return total_dist

