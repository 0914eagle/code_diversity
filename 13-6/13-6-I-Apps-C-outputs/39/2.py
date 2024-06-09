
def solve(connections, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for connection in connections:
        # Add the cost of the flight to the dictionary
        costs[connection[0], connection[1]] = connection[2]
        costs[connection[1], connection[0]] = connection[2]

    # Initialize a set to store the airports that have been visited
    visited = set()
    visited.add(1)  # Add Stockholm as the starting airport

    # Initialize a queue to store the airports to be visited
    queue = [1]

    # Loop until all airports have been visited
    while queue:
        # Get the current airport from the queue
        current_airport = queue.pop(0)

        # Loop through the connections for the current airport
        for connection in connections:
            # Check if the connection is valid and has not been visited yet
            if connection[0] == current_airport and connection[1] not in visited:
                # Add the cost of the flight to the total cost
                costs[current_airport, connection[1]] += costs[current_airport, connection[0]]
                costs[connection[1], current_airport] += costs[current_airport, connection[0]]

                # Add the airport to the queue and visited set
                queue.append(connection[1])
                visited.add(connection[1])

    # Loop through the additional flights
    for flight in additional_flights:
        # Check if the flight is valid and has not been visited yet
        if flight[0] in visited and flight[1] not in visited:
            # Add the cost of the flight to the total cost
            costs[flight[0], flight[1]] += flight[2]
            costs[flight[1], flight[0]] += flight[2]

            # Add the airport to the visited set
            visited.add(flight[1])

    # Return the lowest total cost of flight tickets
    return min(costs.values())

