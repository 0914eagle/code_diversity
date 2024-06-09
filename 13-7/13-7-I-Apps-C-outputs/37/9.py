
def solve(G, K, R, roads, gigs):
    # Initialize a graph with the given number of vertices and edges
    graph = [[] for _ in range(K + 1)]
    for (u, v, w) in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Initialize a dictionary to store the maximum amount of cryptocents that can be earned by playing each gig
    max_cryptocents = {i: 0 for i in range(1, K + 1)}
    
    # Loop through each gig and calculate the maximum amount of cryptocents that can be earned by playing it
    for i in range(G):
        (v, s, e, m) = gigs[i]
        for (u, w) in graph[v]:
            if s <= w <= e:
                max_cryptocents[u] = max(max_cryptocents[u], m)
    
    # Return the maximum amount of cryptocents that can be earned by playing any gig
    return max(max_cryptocents.values())

