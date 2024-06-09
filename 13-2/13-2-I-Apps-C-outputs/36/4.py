
def get_lowest_cost(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight] = flights[flight]
    for flight in additional_flights:
        flight_costs[flight] = additional_flights[flight]
    
    # Initialize a set to store the flights that have been taken
    taken_flights = set()
    
    # Initialize a variable to store the lowest cost
    lowest_cost = float('inf')
    
    # Iterate through all possible combinations of flights
    for i in range(len(flights)):
        for j in range(i+1, len(flights)):
            # Check if the combination of flights forms a cycle
            if flights[i][0] == flights[j][1] and flights[j][0] == flights[i][1]:
                # Calculate the total cost of the combination of flights
                total_cost = flight_costs[flights[i]] + flight_costs[flights[j]]
                # Check if the total cost is lower than the current lowest cost
                if total_cost < lowest_cost:
                    # Update the lowest cost
                    lowest_cost = total_cost
                    # Add the flights to the set of taken flights
                    taken_flights.add(flights[i])
                    taken_flights.add(flights[j])
    
    # Return the lowest cost
    return lowest_cost

def main():
    # Read the input
    num_airports, num_flights = map(int, input().split())
    flights = {}
    for i in range(num_flights):
        a, b, c = map(int, input().split())
        flights[(a, b)] = c
    
    num_additional_flights = int(input())
    additional_flights = {}
    for i in range(num_additional_flights):
        a, b, c = map(int, input().split())
        additional_flights[(a, b)] = c
    
    # Calculate the lowest cost
    lowest_cost = get_lowest_cost(flights, additional_flights)
    
    # Print the lowest cost
    print(lowest_cost)

if __name__ == '__main__':
    main()

