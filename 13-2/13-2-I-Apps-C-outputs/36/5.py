
def get_lowest_cost(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for flight in flights:
        costs[flight] = flights[flight]
    for flight in additional_flights:
        costs[flight] = additional_flights[flight]
    
    # Initialize a set to store the flights that have been taken
    taken_flights = set()
    
    # Initialize a variable to store the lowest cost
    lowest_cost = float('inf')
    
    # Loop through all possible combinations of flights
    for i in range(len(flights)):
        for j in range(i+1, len(flights)):
            # Check if the flights are valid and have not been taken already
            if flights[i] != flights[j] and flights[i] not in taken_flights and flights[j] not in taken_flights:
                # Calculate the total cost of the flights
                total_cost = costs[flights[i]] + costs[flights[j]]
                # Check if the total cost is lower than the current lowest cost
                if total_cost < lowest_cost:
                    # Update the lowest cost
                    lowest_cost = total_cost
    
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
    
    # Print the output
    print(lowest_cost)

if __name__ == '__main__':
    main()

