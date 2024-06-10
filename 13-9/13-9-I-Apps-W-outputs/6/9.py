
def get_min_cost(n, coordinates, city_types):
    # Initialize variables
    total_cost = 0
    cable_count = 0
    prev_city = 0
    prev_type = city_types[0]

    # Iterate through the cities
    for i in range(1, n):
        city = coordinates[i]
        type = city_types[i]

        # If the current city is of a different type than the previous city, we need to connect them with a cable
        if type != prev_type:
            total_cost += abs(city - prev_city)
            cable_count += 1

        # Update the previous city and type
        prev_city = city
        prev_type = type

    return total_cost

def solve(n, coordinates, city_types):
    # Initialize variables
    min_cost = float('inf')
    min_cable_count = 0

    # Iterate through all possible combinations of cables
    for i in range(n):
        # If the current city is not a disputed city, skip it
        if city_types[i] != 'P':
            continue

        # Get the cost of connecting the cities before and after the current city with a cable
        cost_before = get_min_cost(i, coordinates[:i], city_types[:i])
        cost_after = get_min_cost(n - i, coordinates[i:], city_types[i:])

        # Update the minimum cost and cable count if necessary
        total_cost = cost_before + cost_after
        if total_cost < min_cost:
            min_cost = total_cost
            min_cable_count = i

    return min_cable_count

def main():
    n = int(input())
    coordinates = [int(input()) for i in range(n)]
    city_types = [input() for i in range(n)]
    print(solve(n, coordinates, city_types))

if __name__ == '__main__':
    main()

