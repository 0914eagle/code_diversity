
def get_min_cost(cities):
    # Initialize variables
    min_cost = 0
    connected_cities = []

    # Iterate through each city
    for city in cities:
        # If the city is not connected, find the closest connected city and calculate the cost
        if city not in connected_cities:
            closest_city = find_closest_city(city, connected_cities)
            cost = abs(city - closest_city)
            min_cost += cost
            connected_cities.append(city)

    return min_cost

def find_closest_city(city, connected_cities):
    # Initialize variables
    closest_city = None
    min_distance = float('inf')

    # Iterate through each connected city
    for connected_city in connected_cities:
        # Calculate the distance between the current city and the connected city
        distance = abs(city - connected_city)
        # If the distance is less than the current minimum distance, update the minimum distance and closest city
        if distance < min_distance:
            min_distance = distance
            closest_city = connected_city

    return closest_city

def main():
    # Read the number of cities
    n = int(input())
    # Read the cities
    cities = []
    for i in range(n):
        city = int(input())
        cities.append(city)
    # Find the minimum cost
    min_cost = get_min_cost(cities)
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

