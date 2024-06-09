
def solve(connections, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for connection in connections:
        # Add the cost of the flight to the dictionary
        costs[connection[0]] = connection[2]
    
    # Initialize a set to store the airports that have been visited
    visited = set()
    # Initialize a list to store the flights to visit
    flights_to_visit = []
    
    # Add the first airport to the visited set and the flights to visit list
    visited.add(1)
    flights_to_visit.extend(connections)
    
    # Loop through the additional flights
    for flight in additional_flights:
        # If the destination airport has not been visited, add it to the visited set and the flights to visit list
        if flight[1] not in visited:
            visited.add(flight[1])
            flights_to_visit.append(flight)
    
    # Sort the flights to visit list by cost in ascending order
    flights_to_visit.sort(key=lambda x: x[2])
    
    # Initialize a variable to store the total cost of the flights
    total_cost = 0
    
    # Loop through the flights to visit list
    for flight in flights_to_visit:
        # If the destination airport has not been visited, add the cost of the flight to the total cost
        if flight[1] not in visited:
            total_cost += flight[2]
            visited.add(flight[1])
    
    # Return the total cost of the flights
    return total_cost

