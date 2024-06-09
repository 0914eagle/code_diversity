
def get_min_cost(flight_connections, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flight_connections:
        cost = flight[2]
        flight_costs[(flight[0], flight[1])] = cost
        flight_costs[(flight[1], flight[0])] = cost

    # Initialize a set to store the cities that have been reviewed
    reviewed_cities = set()

    # Initialize a minimum spanning tree with the cost of 0
    mst = 0

    # Loop through the additional flights
    for flight in additional_flights:
        # Check if the flight has not been reviewed yet
        if (flight[0], flight[1]) not in reviewed_cities and (flight[1], flight[0]) not in reviewed_cities:
            # Add the cost of the flight to the minimum spanning tree
            mst += flight_costs[(flight[0], flight[1])]
            # Add the cities to the set of reviewed cities
            reviewed_cities.add((flight[0], flight[1]))
            reviewed_cities.add((flight[1], flight[0]))

    # Return the minimum spanning tree cost
    return mst

