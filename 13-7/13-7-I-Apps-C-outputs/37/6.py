
def solve(G, K, R, roads, gigs):
    # Initialize a graph with the given number of vertices and edges
    graph = [[] for _ in range(K + 1)]
    for (u, v, w) in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Initialize a dictionary to store the maximum amount of cryptocents that can be earned by playing a gig at each venue
    max_cryptocents = {1: 0}
    
    # Loop through each gig and calculate the maximum amount of cryptocents that can be earned by playing it
    for (venue, start, end, cryptocents) in gigs:
        if venue not in max_cryptocents:
            max_cryptocents[venue] = 0
        max_cryptocents[venue] = max(max_cryptocents[venue], cryptocents)
    
    # Loop through each venue and calculate the maximum amount of cryptocents that can be earned by playing a gig at that venue
    for venue in range(1, K + 1):
        if venue not in max_cryptocents:
            max_cryptocents[venue] = 0
        for (neighbor, weight) in graph[venue]:
            max_cryptocents[venue] = max(max_cryptocents[venue], max_cryptocents[neighbor] + weight)
    
    # Return the maximum amount of cryptocents that can be earned by playing any gig
    return max(max_cryptocents.values())

