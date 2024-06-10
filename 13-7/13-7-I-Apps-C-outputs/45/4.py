
def get_shortest_time(cities):
    # Initialize a dictionary to store the shortest time from city 1 to each city
    shortest_time = {1: 0}
    for city in range(2, len(cities) + 1):
        # Initialize the shortest time from city 1 to city 'city' as infinite
        shortest_time[city] = float('inf')
        # Iterate over the cities that can be reached from city 'city - 1'
        for prev_city in range(1, city):
            # If the time from city 1 to city 'prev_city' plus the time from city 'prev_city' to city 'city' is less than the current shortest time, update the shortest time
            if shortest_time[prev_city] + cities[prev_city - 1][1] < shortest_time[city]:
                shortest_time[city] = shortest_time[prev_city] + cities[prev_city - 1][1]
    # Return the shortest time from city 1 to each city
    return shortest_time

def get_shortest_path(cities):
    # Initialize a dictionary to store the shortest path from city 1 to each city
    shortest_path = {1: [1]}
    for city in range(2, len(cities) + 1):
        # Initialize the shortest path from city 1 to city 'city' as empty
        shortest_path[city] = []
        # Iterate over the cities that can be reached from city 'city - 1'
        for prev_city in range(1, city):
            # If the time from city 1 to city 'prev_city' plus the time from city 'prev_city' to city 'city' is less than the current shortest time, update the shortest path
            if shortest_path[prev_city] + cities[prev_city - 1][1] < shortest_path[city]:
                shortest_path[city] = shortest_path[prev_city] + [city]
    # Return the shortest path from city 1 to each city
    return shortest_path

def main():
    # Read the number of cities and the cities from stdin
    num_cities = int(input())
    cities = []
    for _ in range(num_cities):
        cities.append(list(map(int, input().split())))
    # Get the shortest time and shortest path from city 1 to each city
    shortest_time = get_shortest_time(cities)
    shortest_path = get_shortest_path(cities)
    # Print the shortest time and shortest path from city 1 to each city
    for city in range(2, len(cities) + 1):
        print(shortest_time[city])
        print(shortest_path[city])

if __name__ == '__main__':
    main()

