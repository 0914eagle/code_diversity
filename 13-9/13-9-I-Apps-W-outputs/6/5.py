
def get_min_cost(n, x, c):
    # Initialize the minimum cost to be infinity
    min_cost = float('inf')
    
    # Loop through all possible combinations of cities to connect
    for i in range(n):
        for j in range(i+1, n):
            # If the cities are of the same type, continue
            if c[i] == c[j]:
                continue
            # If the cities are of different types, calculate the cost of connecting them
            cost = abs(x[i] - x[j])
            # If the cost is less than the minimum cost, update the minimum cost
            if cost < min_cost:
                min_cost = cost
    
    # Return the minimum cost
    return min_cost

def get_connected_cities(n, x, c):
    # Initialize the connected cities to be an empty list
    connected_cities = []
    
    # Loop through all possible combinations of cities to connect
    for i in range(n):
        for j in range(i+1, n):
            # If the cities are of the same type, continue
            if c[i] == c[j]:
                continue
            # If the cities are of different types, calculate the cost of connecting them
            cost = abs(x[i] - x[j])
            # If the cost is less than the minimum cost, update the minimum cost
            if cost < min_cost:
                min_cost = cost
                # Add the connected cities to the list
                connected_cities.append((i, j))
    
    # Return the list of connected cities
    return connected_cities

def get_min_connected_cities(n, x, c):
    # Get the minimum cost of connecting the cities
    min_cost = get_min_cost(n, x, c)
    # Get the list of connected cities
    connected_cities = get_connected_cities(n, x, c)
    # Return the minimum cost and the list of connected cities
    return min_cost, connected_cities

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    c = list(input())
    min_cost, connected_cities = get_min_connected_cities(n, x, c)
    print(min_cost)
    print(connected_cities)

