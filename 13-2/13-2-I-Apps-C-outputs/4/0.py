
def solve(gigs, venues, roads, gig_offers):
    # Initialize a graph to store the connections between venues
    graph = [[] for _ in range(venues + 1)]

    # Add the roads to the graph
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

    # Initialize a dictionary to store the distances from the start node
    distances = {start: 0}

    # Initialize a dictionary to store the previous node for each node
    previous = {start: None}

    # Loop until the priority queue is empty
    while pq:
        # Get the node with the shortest distance from the priority queue
        current_node, current_distance = heapq.heappop(pq)

        # If the current node is the end node, return the path
        if current_node == end:
            path = []
            while previous[current_node] is not None:
                path.append(current_node)
                current_node = previous[current_node]
            path.append(start)
            path.reverse()
            return path

        # If the current node has not been visited
        if current_node not in distances:
            # Mark the current node as visited and add it to the dictionary
            distances[current_node] = current_distance
            previous[current_node] = previous[current_node]

            # Get the neighbors of the current node
            neighbors = graph[current_node]

            # Loop through the neighbors
            for neighbor, weight in neighbors:
                # If the neighbor has not been visited
                if neighbor not in distances:
                    # Calculate the distance to the neighbor
                    distance = current_distance + weight

                    # If the distance is less than the current distance to the neighbor
                    if distance < distances.get(neighbor, float('inf')):
                        # Update the distance to the neighbor
                        distances[neighbor] = distance

                        # Update the previous node for the neighbor
                        previous[neighbor] = current_node

                        # Add the neighbor to the priority queue
                        heapq.heappush(pq, (distance, neighbor))

    # If the end node has not been found, return None
    return None

