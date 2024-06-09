
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for flight in flights:
        costs[flight] = flights[flight]
    for flight in additional_flights:
        costs[flight] = additional_flights[flight]
    
    # Initialize a set to store the airports that have been visited
    visited = set()
    
    # Initialize the total cost variable
    total_cost = 0
    
    # Loop through the flights and calculate the total cost
    for flight in flights:
        # If the airport has not been visited, visit it and add the cost to the total cost
        if flight[0] not in visited:
            total_cost += costs[flight]
            visited.add(flight[0])
        # If the airport has been visited, return to Stockholm and add the cost to the total cost
        elif flight[1] not in visited:
            total_cost += costs[flight]
            visited.add(flight[1])
    
    # Return the total cost
    return total_cost

