
def solve(gigs, venues, roads, travel_time):
    # Initialize a graph to represent the venues and roads
    graph = {}
    for i in range(1, venues + 1):
        graph[i] = []
    for i in range(roads):
        road = roads[i]
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))
    
    # Initialize a dictionary to store the gig offers
    gig_offers = {}
    for i in range(gigs):
        gig = gigs[i]
        gig_offers[gig[0]] = (gig[1], gig[2], gig[3])
    
    # Use a dynamic programming approach to find the maximum number of cryptocents that can be earned
    dp = [0] * (venues + 1)
    for i in range(1, venues + 1):
        for j in graph[i]:
            dp[i] = max(dp[i], dp[j[0]] + gig_offers[i][2])
    
    return dp[venues]

