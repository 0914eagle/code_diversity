
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        cost = flight[2]
        flight_costs[(flight[0], flight[1])] = cost
        flight_costs[(flight[1], flight[0])] = cost

    # Initialize a set to store the cities that have been visited
    visited_cities = set()

    # Initialize the total cost of the flights
    total_cost = 0

    # Loop through the additional flights
    for flight in additional_flights:
        # Check if the flight has already been visited
        if (flight[0], flight[1]) in visited_cities or (flight[1], flight[0]) in visited_cities:
            continue

        # Add the cost of the flight to the total cost
        total_cost += flight[2]

        # Add the cities to the set of visited cities
        visited_cities.add((flight[0], flight[1]))
        visited_cities.add((flight[1], flight[0]))

    # Return the total cost of the flights
    return total_cost

