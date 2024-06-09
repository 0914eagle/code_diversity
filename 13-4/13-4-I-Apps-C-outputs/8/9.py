
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        cost = flight[2]
        flight_costs[(flight[0], flight[1])] = cost
        flight_costs[(flight[1], flight[0])] = cost

    # Initialize a set to store the airports that have been visited
    visited_airports = set()

    # Initialize a list to store the flights that have been taken
    taken_flights = []

    # Loop through the additional flights and take the flights that are not in the list of flights to review
    for flight in additional_flights:
        if (flight[0], flight[1]) not in flight_costs and (flight[1], flight[0]) not in flight_costs:
            taken_flights.append(flight)
            visited_airports.add(flight[0])
            visited_airports.add(flight[1])

    # Loop through the flights to review and take the flights that are not in the list of additional flights
    for flight in flights:
        if (flight[0], flight[1]) not in flight_costs and (flight[1], flight[0]) not in flight_costs:
            taken_flights.append(flight)
            visited_airports.add(flight[0])
            visited_airports.add(flight[1])

    # Loop through the list of airports and take the flights that connect them to Stockholm
    for airport in visited_airports:
        if (airport, 1) not in flight_costs and (1, airport) not in flight_costs:
            taken_flights.append((airport, 1, flight_costs[(airport, 1)]))

    # Calculate the total cost of the flights
    total_cost = 0
    for flight in taken_flights:
        total_cost += flight[2]

    return total_cost

