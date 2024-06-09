
def get_network_coverage(cities, capacities):
    # Initialize variables
    total_coverage = 0
    covered_cities = set()

    # Iterate over each city and its capacity
    for city, capacity in zip(cities, capacities):
        # If the city is already covered, skip it
        if city in covered_cities:
            continue
        # If the city is not covered, add its capacity to the total coverage
        total_coverage += capacity
        # Add the city to the set of covered cities
        covered_cities.add(city)

    # If all cities are covered, return YES, otherwise return NO
    if len(covered_cities) == len(cities):
        return "YES"
    else:
        return "NO"

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate over each test case
    for _ in range(num_test_cases):
        # Read the number of cities and stations
        num_cities = int(input())

        # Read the number of households in each city
        cities = [int(x) for x in input().split()]

        # Read the capacities of each station
        capacities = [int(x) for x in input().split()]

        # Check if the stations can cover all the cities
        result = get_network_coverage(cities, capacities)

        # Print the result
        print(result)

if __name__ == '__main__':
    main()

