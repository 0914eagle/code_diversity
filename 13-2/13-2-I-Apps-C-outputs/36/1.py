
def get_lowest_cost(flights, additional_flights, num_reviews):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight[0]] = flight[2]
    
    # Add the additional flights to the dictionary
    for flight in additional_flights:
        flight_costs[flight[0]] = flight[2]
    
    # Initialize a set to store the cities that have been visited
    visited_cities = set()
    
    # Initialize a list to store the total cost of the flights
    total_cost = []
    
    # Loop through the flights and calculate the total cost
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
        
        # Calculate the total cost of the flight
        total_cost.append(flight_costs[current_city] + flight_costs[next_city])
    
    # Return the lowest total cost
    return min(total_cost)

def main():
    # Read the input from stdin
    num_cities, num_flights = map(int, input().split())
    flights = [list(map(int, input().split())) for _ in range(num_flights)]
    num_additional_flights = int(input())
    additional_flights = [list(map(int, input().split())) for _ in range(num_additional_flights)]
    
    # Call the get_lowest_cost function and print the result
    print(get_lowest_cost(flights, additional_flights, num_cities))

if __name__ == '__main__':
    main()

