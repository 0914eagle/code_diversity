
def is_tourist_friendly(n, roads):
    # Initialize a visited array and a parent array
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    
    # Start from the first city and do a DFS traversal
    city = 1
    visited[city] = True
    for road in roads:
        if road[0] == city:
            city = road[1]
            break
    
    # DFS traversal
    while city != 0:
        for road in roads:
            if road[0] == city and not visited[road[1]]:
                visited[road[1]] = True
                parent[road[1]] = city
                city = road[1]
                break
        else:
            city = parent[city]
    
    # Check if all cities are visited
    for i in range(1, n + 1):
        if not visited[i]:
            return False
    
    return True

def solve(n, roads):
    # Check if the given road network is tourist-friendly
    if is_tourist_friendly(n, roads):
        return "YES"
    
    # If not, try to redirect some of the roads to make it tourist-friendly
    for i in range(len(roads)):
        for j in range(i + 1, len(roads)):
            if roads[i][0] == roads[j][1] and roads[i][1] == roads[j][0]:
                # Redirect the road between the two cities
                roads[i][0], roads[i][1] = roads[i][1], roads[i][0]
                roads[j][0], roads[j][1] = roads[j][1], roads[j][0]
                if is_tourist_friendly(n, roads):
                    return "YES"
                # Undo the changes if it doesn't work
                roads[i][0], roads[i][1] = roads[i][1], roads[i][0]
                roads[j][0], roads[j][1] = roads[j][1], roads[j][0]
    
    return "NO"

