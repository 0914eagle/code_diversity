
def get_min_cost(flights, additional_flights, num_reviews):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight[0]] = flight[2]
    
    # Add the additional flights to the dictionary
    for flight in additional_flights:
        flight_costs[flight[0]] = flight[2]
    
    # Initialize a set to store the airports that have been visited
    visited_airports = set()
    
    # Initialize a variable to store the total cost
    total_cost = 0
    
    # Loop through the flights to review
    for i in range(num_reviews):
        # Get the current airport and the next airport
        current_airport = flights[i][0]
        next_airport = flights[i][1]
        
        # If the current airport has not been visited, add it to the set of visited airports
        if current_airport not in visited_airports:
            visited_airports.add(current_airport)
        
        # Add the cost of the flight to the total cost
        total_cost += flight_costs[current_airport]
        
        # If the next airport has not been visited, add it to the set of visited airports
        if next_airport not in visited_airports:
            visited_airports.add(next_airport)
    
    # Return the total cost
    return total_cost

def main():
    # Read the input
    num_airports, num_flights, num_additional_flights = map(int, input().split())
    flights = []
    for i in range(num_flights):
        flights.append(list(map(int, input().split())))
    additional_flights = []
    for i in range(num_additional_flights):
        additional_flights.append(list(map(int, input().split())))
    
    # Call the get_min_cost function
    total_cost = get_min_cost(flights, additional_flights, num_flights)
    
    # Print the output
    print(total_cost)

if __name__ == '__main__':
    main()

