
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for flight in flights:
        cost = flight[2]
        costs[flight[0], flight[1]] = cost
        costs[flight[1], flight[0]] = cost

    # Initialize a set to store the cities that have been visited
    visited = set()

    # Initialize the total cost variable
    total_cost = 0

    # Loop through the additional flights
    for flight in additional_flights:
        # If the flight has not been visited yet, add it to the visited set and add the cost to the total cost
        if flight[0] not in visited and flight[1] not in visited:
            visited.add(flight[0])
            visited.add(flight[1])
            total_cost += flight[2]

    # Loop through the flights to review
    for flight in flights:
        # If the flight has not been visited yet, add it to the visited set and add the cost to the total cost
        if flight[0] not in visited and flight[1] not in visited:
            visited.add(flight[0])
            visited.add(flight[1])
            total_cost += costs[flight[0], flight[1]]

    return total_cost

