
def solve(gigs, venues, roads, travel_time):
    # Initialize a graph to store the connections between venues
    graph = [[] for _ in range(venues + 1)]

    # Add the roads to the graph
    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))

    # Initialize a dictionary to store the gig offers
    gig_offers = {}

    # Add the gigs to the dictionary
    for gig in gigs:
        gig_offers[gig[0]] = (gig[1], gig[2], gig[3])

    # Initialize a variable to store the maximum amount of cryptocents that can be earned
    max_cryptocents = 0

    # Iterate over the gig offers
    for gig in gig_offers:
        # If the gig is at the current venue
        if gig == venue:
            # Add the amount of cryptocents earned by playing the gig to the maximum amount
            max_cryptocents += gig_offers[gig][2]
        # If the gig is at a different venue
        else:
            # Find the shortest path between the current venue and the gig venue
            path = dijkstra(graph, venue, gig)

            # If there is a path between the current venue and the gig venue
            if path:
                # Add the amount of cryptocents earned by playing the gig to the maximum amount
                max_cryptocents += gig_offers[gig][2]

                # Update the current venue to the gig venue
                venue = gig

    return max_cryptocents

