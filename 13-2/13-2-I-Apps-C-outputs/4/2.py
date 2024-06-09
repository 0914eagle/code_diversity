
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
        venue, start_time, end_time, cryptocents = gigs_dict[gig[0]]

        # If the gig is at the current venue, add the cryptocents to the maximum amount
        if venue == 1:
            max_cryptocents += cryptocents

        # If the gig is at a different venue, calculate the time it takes to travel to that venue and add the cryptocents if it's faster than the current maximum
        else:
            travel_time_to_venue = get_travel_time(graph, 1, venue, travel_time)
            if travel_time_to_venue + start_time <= end_time:
                max_cryptocents += cryptocents

    return max_cryptocents

def get_travel_time(graph, start_venue, end_venue, travel_time):
    # Initialize a queue to store the venues to visit
    queue = [start_venue]

    # Initialize a dictionary to store the visited venues
    visited = {start_venue: True}

    # Initialize a variable to store the travel time
    travel_time_to_venue = 0

    # While there are still venues to visit
    while queue:
        # Get the current venue
        current_venue = queue.pop(0)

        # If the current venue is the end venue, return the travel time
        if current_venue == end_venue:
            return travel_time_to_venue

        # Iterate over the neighbors of the current venue
        for neighbor, time in graph[current_venue]:
            # If the neighbor has not been visited, add it to the queue and mark it as visited
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = True

                # Add the travel time to the total travel time
                travel_time_to_venue += time

    # If the end venue was not found, return -1
    return -1

