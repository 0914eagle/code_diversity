
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight] = flights[flight]
    for flight in additional_flights:
        flight_costs[flight] = additional_flights[flight]

    # Initialize a set to store the cities that have been visited
    visited_cities = set()

    # Initialize a variable to store the total cost of the flights
    total_cost = 0

    # Loop through the flights and calculate the total cost
    for flight in flights:
        # If the flight is not in the visited_cities set, add it to the total cost and mark the city as visited
        if flight[0] not in visited_cities:
            total_cost += flight_costs[flight]
            visited_cities.add(flight[0])
        # If the flight is not in the visited_cities set, add it to the total cost and mark the city as visited
        if flight[1] not in visited_cities:
            total_cost += flight_costs[flight]
            visited_cities.add(flight[1])

    return total_cost

