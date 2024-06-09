
def get_expected_length(n, roads):
    # Initialize a dictionary to store the distances between each pair of cities
    distances = {}
    for road in roads:
        city1, city2 = road[0], road[1]
        if city1 not in distances:
            distances[city1] = {}
        distances[city1][city2] = 1
        if city2 not in distances:
            distances[city2] = {}
        distances[city2][city1] = 1
    
    # Initialize a set to store the cities that have been visited
    visited_cities = set()
    visited_cities.add(1)
    
    # Initialize a list to store the expected lengths of each city
    expected_lengths = [0] * (n + 1)
    expected_lengths[1] = 0
    
    # Loop through each city and calculate the expected length of reaching it
    for city in range(1, n + 1):
        if city not in visited_cities:
            visited_cities.add(city)
            for neighbor in distances[city]:
                if neighbor not in visited_cities:
                    expected_lengths[neighbor] += expected_lengths[city] / len(distances[city])
    
    # Return the expected length of the journey
    return sum(expected_lengths)

def main():
    n = int(input())
    roads = []
    for i in range(n - 1):
        road = list(map(int, input().split()))
        roads.append(road)
    print(get_expected_length(n, roads))

if __name__ == '__main__':
    main()

