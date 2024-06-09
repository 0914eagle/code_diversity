
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight[0]] = flight[2]
    
    # Initialize a dictionary to store the cost of each additional flight
    additional_flight_costs = {}
    for flight in additional_flights:
        additional_flight_costs[flight[0]] = flight[2]
    
    # Initialize a set to store the airports that have been visited
    visited_airports = set()
    
    # Initialize a variable to store the total cost of the flights
    total_cost = 0
    
    # Loop through the flights to review
    for flight in flights:
        # If the airport has not been visited, visit it and add the cost of the flight to the total cost
        if flight[0] not in visited_airports:
            visited_airports.add(flight[0])
            total_cost += flight_costs[flight[0]]
        # If the airport has been visited, check if the additional flight cost is lower than the current cost
        else:
            if additional_flight_costs[flight[0]] < flight_costs[flight[0]]:
                total_cost += additional_flight_costs[flight[0]]
            else:
                total_cost += flight_costs[flight[0]]
    
    # Return the total cost of the flights
    return total_cost

