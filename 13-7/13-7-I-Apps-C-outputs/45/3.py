
def get_shortest_time(cities, start_city):
    # Initialize a dictionary to store the shortest time from the start city to each city
    shortest_time = {start_city: 0}

    # Loop through all cities
    for city in cities:
        # If the city is not the start city, check if it has already been visited
        if city != start_city and city not in shortest_time:
            # If the city has not been visited, find the shortest time to visit it from the start city
            shortest_time[city] = find_shortest_time(cities, start_city, city)

    # Return the shortest time from the start city to each city
    return shortest_time

def find_shortest_time(cities, start_city, end_city):
    # Initialize the shortest time to infinity
    shortest_time = float('inf')

    # Loop through all cities between the start and end cities
    for city in range(start_city + 1, end_city):
        # If the city is not the end city, check if it has already been visited
        if city != end_city and city not in shortest_time:
            # If the city has not been visited, find the shortest time to visit it from the start city
            time = find_shortest_time(cities, start_city, city) + cities[city][1] + cities[city][2]

            # If the time is less than the current shortest time, update the shortest time
            if time < shortest_time:
                shortest_time = time

    # Return the shortest time to visit the end city from the start city
    return shortest_time

def main():
    # Read the number of cities and their coordinates, distance, and travel time
    num_cities = int(input())
    cities = {}
    for i in range(num_cities):
        city = int(input())
        coordinates, distance, travel_time = map(int, input().split())
        cities[city] = (coordinates, distance, travel_time)

    # Get the shortest time to visit each city from the start city
    shortest_time = get_shortest_time(cities, 1)

    # Print the shortest time to visit each city
    for i in range(num_cities - 1):
        print(shortest_time[i + 2])

if __name__ == '__main__':
    main()

