
def solve(gigs, venues, roads, time):
    # Initialize a list to store the maximum amount of cryptocents that can be earned at each venue
    max_cryptocents = [0] * (venues + 1)
    # Initialize a list to store the minimum time required to travel between each pair of venues
    min_time = [[0] * (venues + 1) for _ in range(venues + 1)]
    
    # Fill in the minimum time required to travel between each pair of venues
    for i in range(roads):
        road = roads[i]
        min_time[road[0]][road[1]] = min_time[road[1]][road[0]] = road[2]
    
    # Fill in the maximum amount of cryptocents that can be earned at each venue
    for i in range(gigs):
        gig = gigs[i]
        max_cryptocents[gig[0]] = max(max_cryptocents[gig[0]], gig[3])
    
    # Use dynamic programming to find the maximum amount of cryptocents that can be earned by taking on the right gigs
    for i in range(time, -1, -1):
        for j in range(1, venues + 1):
            max_cryptocents[j] = max(max_cryptocents[j], max_cryptocents[j - 1] + max_cryptocents[j])
    
    return max_cryptocents[-1]

