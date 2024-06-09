
def get_min_cost(n, cities):
    # Initialize variables
    min_cost = 0
    visited = [False] * n
    visited[0] = True

    # Loop through all cities
    for i in range(n):
        # If the current city is not visited, visit it and update the minimum cost
        if not visited[i]:
            min_cost += dfs(cities, visited, i)

    return min_cost

def dfs(cities, visited, curr):
    # Mark the current city as visited
    visited[curr] = True
    cost = 0

    # Loop through all neighboring cities
    for neighbor in get_neighbors(cities, curr):
        # If the neighboring city is not visited, visit it and update the minimum cost
        if not visited[neighbor]:
            cost += dfs(cities, visited, neighbor)

    return cost

def get_neighbors(cities, curr):
    # Get the coordinates of the current city
    x, y = cities[curr]

    # Initialize a list to store the neighboring cities
    neighbors = []

    # Loop through all cities
    for i in range(len(cities)):
        # If the current city is not the same as the previous city
        if i != curr:
            # Get the coordinates of the current city
            x_neighbor, y_neighbor = cities[i]

            # If the neighboring city is within the range of the current city
            if abs(x_neighbor - x) <= 1 and abs(y_neighbor - y) <= 1:
                # Add the neighboring city to the list of neighbors
                neighbors.append(i)

    return neighbors

def main():
    n = int(input())
    cities = []
    for i in range(n):
        x, c = input().split()
        cities.append((int(x), c))
    print(get_min_cost(n, cities))

if __name__ == '__main__':
    main()

