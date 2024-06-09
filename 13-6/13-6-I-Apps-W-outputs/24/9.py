
def get_min_cable_length(cities):
    # Initialize variables
    min_length = 0
    prev_city = None

    # Iterate through the cities
    for city in cities:
        # If this is the first city, set the previous city to it
        if prev_city is None:
            prev_city = city
            continue

        # Calculate the length of the cable between the previous city and the current city
        length = abs(city - prev_city)

        # Add the length to the total length
        min_length += length

        # Set the previous city to the current city
        prev_city = city

    # Return the minimum length
    return min_length

def get_min_cable_length_with_disputed_cities(cities, disputed_cities):
    # Initialize variables
    min_length = 0
    prev_city = None

    # Iterate through the cities
    for city in cities:
        # If this is the first city, set the previous city to it
        if prev_city is None:
            prev_city = city
            continue

        # Calculate the length of the cable between the previous city and the current city
        length = abs(city - prev_city)

        # If the current city is disputed, add the length to the total length
        if city in disputed_cities:
            min_length += length

        # Set the previous city to the current city
        prev_city = city

    # Return the minimum length
    return min_length

def get_min_cable_length_with_disputed_cities_optimized(cities, disputed_cities):
    # Initialize variables
    min_length = 0
    prev_city = None

    # Iterate through the cities
    for city in cities:
        # If this is the first city, set the previous city to it
        if prev_city is None:
            prev_city = city
            continue

        # Calculate the length of the cable between the previous city and the current city
        length = abs(city - prev_city)

        # If the current city is disputed, add the length to the total length
        if city in disputed_cities:
            min_length += length

        # Set the previous city to the current city
        prev_city = city

    # Return the minimum length
    return min_length

def main():
    # Read the input
    n = int(input())
    cities = []
    disputed_cities = []
    for i in range(n):
        city = int(input())
        city_type = input()
        if city_type == 'P':
            disputed_cities.append(city)
        cities.append(city)

    # Calculate the minimum length of cables with disputed cities
    min_length_with_disputed_cities = get_min_cable_length_with_disputed_cities(cities, disputed_cities)

    # Calculate the minimum length of cables without disputed cities
    min_length_without_disputed_cities = get_min_cable_length(cities)

    # Print the minimum length
    print(min(min_length_with_disputed_cities, min_length_without_disputed_cities))

if __name__ == '__main__':
    main()

