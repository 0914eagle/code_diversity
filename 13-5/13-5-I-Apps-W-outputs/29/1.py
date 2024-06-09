
def solve(n, m, a, b, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[roads[i][0] - 1].append(roads[i][1] - 1)
        graph[roads[i][1] - 1].append(roads[i][0] - 1)
    
    # Initialize an array to store the number of soldiers in each city
    soldiers = [0] * n
    
    # Loop through each city and its neighbors
    for i in range(n):
        for j in graph[i]:
            # If the number of soldiers in the current city is greater than the number of soldiers in the neighboring city
            if a[i] > a[j]:
                # Send some soldiers from the current city to the neighboring city
                soldiers[j] += a[i] - a[j]
                a[i] = a[j]
    
    # Check if the number of soldiers in each city is equal to the desired number
    for i in range(n):
        if a[i] != b[i]:
            return "NO"
    
    # If all conditions are met, return the number of soldiers that should stay in each city
    result = []
    for i in range(n):
        result.append([soldiers[i], 0] * n)
        result[i][i] = a[i]
    return "YES\n" + "\n".join(map(str, result))

