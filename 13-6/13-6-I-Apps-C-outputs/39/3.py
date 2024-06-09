
def solve(connections, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for connection in connections:
        # Add the cost of the flight to the dictionary
        costs[connection] = int(connection.split()[2])

    # Initialize a set to store the airports that have been visited
    visited = set()
    # Add Stockholm as the starting airport
    visited.add(1)

    # Initialize a list to store the flights to review
    reviews = []
    for flight in additional_flights:
        # Add the flight to the list of flights to review
        reviews.append(flight)

    # Initialize a variable to store the total cost of the flights
    total_cost = 0
    while reviews:
        # Get the next flight to review
        flight = reviews.pop(0)
        # Get the airports involved in the flight
        airports = flight.split()
        # Check if the starting airport has been visited
        if airports[0] not in visited:
            # Add the cost of the flight to the total cost
            total_cost += costs[flight]
            # Add the starting airport to the set of visited airports
            visited.add(airports[0])
        # Check if the destination airport has been visited
        if airports[1] not in visited:
            # Add the cost of the flight to the total cost
            total_cost += costs[flight]
            # Add the destination airport to the set of visited airports
            visited.add(airports[1])

    # Return the total cost of the flights
    return total_cost

