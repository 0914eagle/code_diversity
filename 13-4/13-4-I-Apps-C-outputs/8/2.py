
def solve(N, R, flights, F, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for flight in flights:
        costs[flight[0]] = flight[2]
    for flight in additional_flights:
        costs[flight[0]] = flight[2]
    
    # Initialize a list to store the flights to review
    reviews = []
    for i in range(R):
        reviews.append(flights[i][0])
    
    # Initialize a list to store the flights to take
    flights_to_take = []
    
    # Loop through the flights to review and add them to the list of flights to take
    for flight in reviews:
        flights_to_take.append(flight)
    
    # Loop through the additional flights and add them to the list of flights to take if they are not already in the list
    for flight in additional_flights:
        if flight[0] not in flights_to_take:
            flights_to_take.append(flight)
    
    # Calculate the total cost of the flights to take
    total_cost = 0
    for flight in flights_to_take:
        total_cost += costs[flight[0]]
    
    return total_cost

