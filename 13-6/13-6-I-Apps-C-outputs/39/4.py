
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight[0]] = flight[2]
    for flight in additional_flights:
        flight_costs[flight[0]] = flight[2]
    
    # Initialize a list to store the flights to review
    reviews = []
    for flight in flights:
        reviews.append(flight[0])
    
    # Initialize a set to store the flights that have been reviewed
    reviewed_flights = set()
    
    # Loop through the flights to review and find the cheapest flight that has not been reviewed yet
    while len(reviews) > 0:
        cheapest_flight = float("inf")
        for flight in reviews:
            if flight not in reviewed_flights and flight_costs[flight] < cheapest_flight:
                cheapest_flight = flight_costs[flight]
                next_flight = flight
        reviewed_flights.add(next_flight)
        reviews.remove(next_flight)
    
    # Return the total cost of the flights
    return sum(flight_costs[flight] for flight in reviewed_flights)

