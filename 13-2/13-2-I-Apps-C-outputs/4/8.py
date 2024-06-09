
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

    # Initialize a variable to store the maximum amount of cryptocents that can be earned
    max_cryptocents = 0

    # Iterate over each gig
    for gig in gigs:
        # Get the details of the gig
        venue, start_time, end_time, cryptocents = gigs_dict[gig]

        # If the gig is at the current venue, add the cryptocents to the maximum amount
        if venue == 1:
            max_cryptocents += cryptocents

        # If the gig is at a different venue, check if it is possible to travel to that venue and play the gig
        else:
            # Get the shortest path from the current venue to the gig venue
            path = dijkstra(graph, 1, venue)

            # If the path exists and the total time taken is less than the start time of the gig, add the cryptocents to the maximum amount
            if path and path[1] <= start_time:
                max_cryptocents += cryptocents

    return max_cryptocents

