
def get_lowest_cost(flights, additional_flights, num_reviews):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight[0]] = flight[2]
    for flight in additional_flights:
        flight_costs[flight[0]] = flight[2]

    # Initialize a set to store the cities that have been visited
    visited_cities = set()

    # Initialize a variable to store the total cost
    total_cost = 0

    # Loop through the flights to review
    for i in range(num_reviews):
        # Get the current city and the next city
        current_city = flights[i][0]
        next_city = flights[i][1]

        # If the current city has not been visited, add it to the visited cities set
        if current_city not in visited_cities:
            visited_cities.add(current_city)

        # If the next city has not been visited, add it to the visited cities set
        if next_city not in visited_cities:
            visited_cities.add(next_city)

        # Add the cost of the current flight to the total cost
        total_cost += flight_costs[current_city]

    # Return the total cost
    return total_cost

def main():
    # Read the input
    num_airports, num_flights = map(int, input().split())
    flights = []
    for i in range(num_flights):
        flights.append(list(map(int, input().split())))
    num_additional_flights = int(input())
    additional_flights = []
    for i in range(num_additional_flights):
        additional_flights.append(list(map(int, input().split())))

    # Call the get_lowest_cost function
    lowest_cost = get_lowest_cost(flights, additional_flights, num_flights)

    # Print the lowest cost
    print(lowest_cost)

if __name__ == '__main__':
    main()

