
def solve(connections, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for connection in connections:
        # Add the cost of the flight to the dictionary
        costs[connection] = connection[2]

    # Initialize a set to store the airports that have been visited
    visited = set()
    visited.add(1) # Add Stockholm as the starting airport

    # Initialize a queue to store the flights to visit
    queue = []

    # Add the first flight to the queue
    queue.append(connections[0])

    # Loop until all the flights have been visited
    while queue:
        # Get the next flight from the queue
        flight = queue.pop(0)

        # Check if the flight has already been visited
        if flight not in visited:
            # Add the cost of the flight to the total cost
            total_cost += costs[flight]

            # Add the airport at the end of the flight to the visited set
            visited.add(flight[1])

            # Add the flight to the queue
            queue.append(flight)

    # Return the total cost of the flights
    return total_cost

