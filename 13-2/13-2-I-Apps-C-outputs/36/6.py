
def get_lowest_cost(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight] = flights[flight]

    # Add the additional flights to the dictionary
    for flight in additional_flights:
        flight_costs[flight] = additional_flights[flight]

    # Find the minimum cost of all flights
    min_cost = min(flight_costs.values())

    # Return the minimum cost
    return min_cost

def main():
    # Read the input
    num_airports, num_flights = map(int, input().split())
    flights = {}
    for _ in range(num_flights):
        a, b, c = map(int, input().split())
        flights[(a, b)] = c
        flights[(b, a)] = c
    num_additional_flights = int(input())
    additional_flights = {}
    for _ in range(num_additional_flights):
        a, b, c = map(int, input().split())
        additional_flights[(a, b)] = c
        additional_flights[(b, a)] = c

    # Call the get_lowest_cost function
    lowest_cost = get_lowest_cost(flights, additional_flights)

    # Print the output
    print(lowest_cost)

if __name__ == '__main__':
    main()

