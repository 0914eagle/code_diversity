
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

    # Iterate through each gig offer
    for i in range(1, venues + 1):
        # If the gig offer is at the current venue
        if i in gig_dict:
            # Get the start and end time of the gig
            start_time, end_time, cryptocents = gig_dict[i]

            # If the gig offer is at the current venue and the start time is 0
            if start_time == 0:
                # Add the cryptocents to the maximum amount
                max_cryptocents += cryptocents

            # If the gig offer is not at the current venue
            else:
                # Get the shortest path from the current venue to the gig offer venue
                path = dijkstra(graph, i, gig_dict[i][0])

                # If the shortest path is not None
                if path:
                    # Get the time it takes to travel to the gig offer venue
                    travel_time = path[1]

                    # If the start time of the gig is after the travel time
                    if start_time > travel_time:
                        # Add the cryptocents to the maximum amount
                        max_cryptocents += cryptocents

    return max_cryptocents


def dijkstra(graph, start, end):
    # Initialize a priority queue to store the nodes to visit
    pq = [(0, start)]

    # Initialize a dictionary to store the distances to each node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Initialize a dictionary to store the previous node for each node
    previous = {node: None for node in graph}

    # Loop until the priority queue is empty
    while pq:
        # Get the node with the shortest distance
        distance, node = heapq.heappop(pq)

        # If the node is the end node, return the path
        if node == end:
            path = []
            while previous[node] is not None:
                path.append(node)
                node = previous[node]
            return [path, distance]

        # If the node has not been visited
        if distances[node] == float("inf"):
            # Loop through the node's neighbors
            for neighbor, weight in graph[node]:
                # If the neighbor has not been visited
                if distances[neighbor] == float("inf"):
                    # Calculate the distance to the neighbor
                    distance_to_neighbor = distance + weight

                    # If the distance to the neighbor is less than the current distance
                    if distance_to_neighbor < distances[neighbor]:
                        # Update the distance to the neighbor
                        distances[neighbor] = distance_to_neighbor

                        # Update the previous node for the neighbor
                        previous[neighbor] = node

                        # Add the neighbor to the priority queue
                        heapq.heappush(pq, (distance_to_neighbor, neighbor))

    # If there is no path, return None
    return None

