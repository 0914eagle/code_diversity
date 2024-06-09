
def expected_length(n, roads):
    # Initialize a dictionary to store the distances between cities
    distances = {}
    for road in roads:
        city1, city2 = road
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}
        distances[city1][city2] = 1
        distances[city2][city1] = 1
    
    # Initialize a set to store the visited cities
    visited = set()
    visited.add(1)
    
    # Initialize a queue to store the cities to visit
    queue = [1]
    
    # Initialize a variable to store the total distance
    total_distance = 0
    
    while queue:
        # Dequeue a city from the queue
        city = queue.pop(0)
        
        # If the city has not been visited before, visit it
        if city not in visited:
            visited.add(city)
            total_distance += 1
            
            # Enqueue the neighboring cities that have not been visited before
            for neighbor in distances[city]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    # Return the total distance
    return total_distance / n

def main():
    n = int(input())
    roads = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        roads.append((u, v))
    print(expected_length(n, roads))

if __name__ == '__main__':
    main()

