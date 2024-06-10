
def get_min_cost(n, cities):
    # Initialize variables
    min_cost = 0
    visited = set()
    queue = []
    
    # Add the first city to the queue
    queue.append(cities[0])
    visited.add(cities[0])
    
    # Loop through the queue
    while queue:
        # Get the current city
        current_city = queue.pop(0)
        
        # Check if the current city is a Byteland city
        if current_city[1] == 'B':
            # Add the cost of the cable to the min_cost
            min_cost += current_city[0]
        
        # Add the neighbors of the current city to the queue
        for neighbor in cities:
            if neighbor[0] > current_city[0] and neighbor[0] not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    # Return the min_cost
    return min_cost

def main():
    # Read the input
    n = int(input())
    cities = []
    for i in range(n):
        x, c = input().split()
        cities.append((int(x), c))
    
    # Call the get_min_cost function
    min_cost = get_min_cost(n, cities)
    
    # Print the result
    print(min_cost)

if __name__ == '__main__':
    main()

