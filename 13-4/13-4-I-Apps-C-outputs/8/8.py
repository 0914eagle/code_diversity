
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
        reviews.append(flights[i])
    
    # Add additional flights to the list of flights to review
    for i in range(F):
        reviews.append(additional_flights[i])
    
    # Sort the list of flights to review by cost
    reviews.sort(key=lambda x: x[2])
    
    # Initialize a variable to store the total cost of flight tickets
    total_cost = 0
    
    # Loop through the list of flights to review
    for i in range(len(reviews)):
        # If the current flight is not from Stockholm, add its cost to the total cost
        if reviews[i][0] != 1:
            total_cost += costs[reviews[i][0]]
    
    return total_cost

