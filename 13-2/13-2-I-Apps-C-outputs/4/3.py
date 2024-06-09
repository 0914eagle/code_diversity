
def solve(gigs, venues, roads, travel_time):
    # Initialize a graph to store the connections between venues
    graph = [[] for _ in range(venues + 1)]

    # Add the roads to the graph
    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))

    # Initialize a dictionary to store the gigs and their details
    gigs_dict = {}
    for gig in gigs:
        gigs_dict[gig[0]] = (gig[1], gig[2], gig[3])

    # Initialize a dictionary to store the maximum amount of cryptocents that can be earned by visiting each venue
    max_cryptocents = {1: 0}

    # Loop through each venue and calculate the maximum amount of cryptocents that can be earned by visiting it
    for venue in range(1, venues + 1):
        if venue not in max_cryptocents:
            max_cryptocents[venue] = 0
        for neighbor, time in graph[venue]:
            if neighbor in max_cryptocents:
                max_cryptocents[venue] = max(max_cryptocents[venue], max_cryptocents[neighbor] + gigs_dict[neighbor][2])
            else:
                max_cryptocents[venue] = max(max_cryptocents[venue], gigs_dict[neighbor][2])

    # Return the maximum amount of cryptocents that can be earned by visiting each venue
    return max(max_cryptocents.values())

