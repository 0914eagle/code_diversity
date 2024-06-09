
def get_lowest_cost(flight_connections, additional_flights, num_reviews):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flight_connections:
        flight_costs[flight] = flight_connections[flight]
    for flight in additional_flights:
        flight_costs[flight] = additional_flights[flight]

    # Initialize a set to store the flights that have been taken
    taken_flights = set()

    # Initialize a variable to store the total cost of the flights
    total_cost = 0

    # Loop through the flights to review
    for i in range(num_reviews):
        # Find the flight with the lowest cost that has not been taken yet
        min_cost = float('inf')
        min_flight = None
        for flight in flight_costs:
            if flight not in taken_flights and flight_costs[flight] < min_cost:
                min_cost = flight_costs[flight]
                min_flight = flight

        # Add the cost of the flight to the total cost
        total_cost += min_cost

        # Add the flight to the set of taken flights
        taken_flights.add(min_flight)

    # Return the total cost of the flights
    return total_cost

def main():
    num_airports, num_reviews = map(int, input().split())
    flight_connections = {}
    for i in range(num_reviews):
        a, b, c = map(int, input().split())
        flight_connections[(a, b)] = c
        flight_connections[(b, a)] = c
    num_additional_flights = int(input())
    additional_flights = {}
    for i in range(num_additional_flights):
        a, b, c = map(int, input().split())
        additional_flights[(a, b)] = c
        additional_flights[(b, a)] = c
    print(get_lowest_cost(flight_connections, additional_flights, num_reviews))

if __name__ == '__main__':
    main()

