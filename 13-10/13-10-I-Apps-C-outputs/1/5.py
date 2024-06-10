
import sys
input = sys.stdin.read()

def get_shortest_paths(n_cities, n_roads, roads):
    # Initialize a dictionary to store the shortest paths from each city to each other city
    shortest_paths = {}
    for i in range(n_cities):
        shortest_paths[i] = {}
        for j in range(n_cities):
            if i == j:
                shortest_paths[i][j] = 0
            else:
                shortest_paths[i][j] = float('inf')

    # Loop through each road and update the shortest paths between the origin and destination cities
    for road in roads:
        origin, destination, length = road
        if shortest_paths[origin][destination] > length:
            shortest_paths[origin][destination] = length
            shortest_paths[destination][origin] = length

    # Loop through each city and find the shortest path to all other cities
    for city in range(n_cities):
        for other_city in range(n_cities):
            if city == other_city:
                continue
            shortest_path = float('inf')
            for intermediate_city in range(n_cities):
                if intermediate_city == city or intermediate_city == other_city:
                    continue
                shortest_path = min(shortest_path, shortest_paths[city][intermediate_city] + shortest_paths[intermediate_city][other_city])
            shortest_paths[city][other_city] = shortest_path

    return shortest_paths

def count_shortest_paths_containing_road(n_cities, n_roads, roads, road):
    # Get the shortest paths between all pairs of cities
    shortest_paths = get_shortest_paths(n_cities, n_roads, roads)

    # Initialize a counter for the number of shortest paths containing the road
    count = 0

    # Loop through each city and count the number of shortest paths from that city to all other cities that contain the road
    for city in range(n_cities):
        for other_city in range(n_cities):
            if city == other_city:
                continue
            if road in shortest_paths[city][other_city]:
                count += 1

    return count % 1000000007

def main():
    n_cities, n_roads = map(int, input.split())
    roads = []
    for i in range(n_roads):
        origin, destination, length = map(int, input.split())
        roads.append((origin, destination, length))
    for road in roads:
        print(count_shortest_paths_containing_road(n_cities, n_roads, roads, road))

if __name__ == '__main__':
    main()

