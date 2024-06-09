
def solve(gigs, venues, roads, gig_offers):
    # Initialize a graph to store the connections between venues
    graph = [[] for _ in range(venues + 1)]

    # Add edges to the graph based on the roads
    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))

    # Initialize a dictionary to store the gig offers
    gig_dict = {}
    for offer in gig_offers:
        gig_dict[offer[0]] = (offer[1], offer[2], offer[3])

    # Initialize a variable to store the maximum amount of cryptocents
    max_cryptocents = 0

    # Loop through each gig offer
    for i in range(1, venues + 1):
        # If the gig offer is at the current venue
        if i in gig_dict:
            # Get the start and end times of the gig
            start_time, end_time, cryptocents = gig_dict[i]

            # If the gig offer is at the current venue and the start time is 0
            if start_time == 0:
                # Add the cryptocents to the maximum amount
                max_cryptocents += cryptocents

                # Remove the gig offer from the dictionary
                del gig_dict[i]

    # Loop through each gig offer
    for i in range(1, venues + 1):
        # If the gig offer is at a different venue
        if i not in gig_dict:
            # Continue to the next gig offer
            continue

        # Get the start and end times of the gig
        start_time, end_time, cryptocents = gig_dict[i]

        # If the gig offer is at a different venue and the start time is not 0
        if start_time != 0:
            # Find the shortest path between the current venue and the gig offer venue
            shortest_path = find_shortest_path(graph, i, start_time)

            # If the shortest path is not None
            if shortest_path is not None:
                # Add the cryptocents to the maximum amount
                max_cryptocents += cryptocents

                # Remove the gig offer from the dictionary
                del gig_dict[i]

    return max_cryptocents

def find_shortest_path(graph, start, target):
    # Initialize a queue to store the nodes to visit
    queue = [(start, 0)]

    # Initialize a dictionary to store the distances from the start node
    distances = {start: 0}

    # Loop until the queue is empty
    while queue:
        # Get the current node and distance from the queue
        node, distance = queue.pop(0)

        # If the current node is the target node
        if node == target:
            # Return the distance
            return distance

        # Loop through the neighbors of the current node
        for neighbor, weight in graph[node]:
            # If the neighbor has not been visited
            if neighbor not in distances:
                # Add the neighbor to the queue
                queue.append((neighbor, distance + weight))

                # Add the neighbor to the dictionary with the current distance
                distances[neighbor] = distance + weight

    # If the target node is not found, return None
    return None

