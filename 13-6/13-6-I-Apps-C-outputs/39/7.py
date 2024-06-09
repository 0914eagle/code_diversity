
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for flight in flights:
        costs[flight] = flights[flight]
    for flight in additional_flights:
        costs[flight] = additional_flights[flight]
    
    # Initialize a set to store the cities that have been visited
    visited = set()
    
    # Initialize a variable to store the total cost
    total_cost = 0
    
    # Loop through the flights and calculate the total cost
    for flight in flights:
        city1, city2 = flight[0], flight[1]
        cost = costs[flight]
        if city1 not in visited:
            visited.add(city1)
            total_cost += cost
        if city2 not in visited:
            visited.add(city2)
            total_cost += cost
    
    return total_cost

