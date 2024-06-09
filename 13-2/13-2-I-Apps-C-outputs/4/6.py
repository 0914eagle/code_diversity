
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

    # Initialize a variable to store the maximum amount of cryptocents
    max_cryptocents = 0

    # Iterate over the gig offers
    for gig in gig_offers:
        # Check if the gig is at the current venue
        if gig == venue:
            # Add the cryptocents to the maximum amount
            max_cryptocents += gig_offers[gig][2]
        # Check if the gig is at a different venue
        else:
            # Calculate the time it takes to travel to the gig venue
            travel_time_to_gig = travel_time(graph, venue, gig)

            # Check if the gig is within the time window
            if gig_offers[gig][0] <= travel_time_to_gig <= gig_offers[gig][1]:
                # Add the cryptocents to the maximum amount
                max_cryptocents += gig_offers[gig][2]

    # Return the maximum amount of cryptocents
    return max_cryptocents

