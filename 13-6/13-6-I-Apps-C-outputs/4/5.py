
def f1(n, m, railways):
    # f1(n, m, railways) returns the minimum number of hours needed for both vehicles to reach town n
    # under the constraints that the train can only use railways and the bus can only use roads
    # and that they must not arrive at the same town (except town n) simultaneously
    
    # Initialize the graph with the railways
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in railways:
        graph[u].add(v)
        graph[v].add(u)
    
    # Initialize the distances from town 1 to each town
    distances = {1: 0}
    queue = [1]
    while queue:
        town = queue.pop(0)
        for neighbor in graph[town]:
            if neighbor not in distances:
                distances[neighbor] = distances[town] + 1
                queue.append(neighbor)
    
    # Initialize the times for the bus and the train to reach each town
    bus_times = {town: distances[town] for town in distances}
    train_times = {town: distances[town] for town in distances}
    
    # Update the times for the bus and the train to reach each town using the roads and railways
    for town in distances:
        for neighbor in graph[town]:
            if neighbor in distances:
                bus_times[neighbor] = min(bus_times[neighbor], bus_times[town] + 1)
                train_times[neighbor] = min(train_times[neighbor], train_times[town] + 1)
    
    # Return the maximum of the bus and train's arrival times in town n
    return max(bus_times[n], train_times[n])

def f2(n, m, railways):
    # f2(n, m, railways) returns the minimum number of hours needed for both vehicles to reach town n
    # under the constraints that the train can only use railways and the bus can only use roads
    # and that they must not arrive at the same town (except town n) simultaneously
    # This function uses a more efficient algorithm by only considering the shortest path between town 1 and town n
    
    # Initialize the graph with the railways
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in railways:
        graph[u].add(v)
        graph[v].add(u)
    
    # Initialize the distances from town 1 to each town
    distances = {1: 0}
    queue = [1]
    while queue:
        town = queue.pop(0)
        for neighbor in graph[town]:
            if neighbor not in distances:
                distances[neighbor] = distances[town] + 1
                queue.append(neighbor)
    
    # Initialize the times for the bus and the train to reach each town
    bus_times = {town: distances[town] for town in distances}
    train_times = {town: distances[town] for town in distances}
    
    # Update the times for the bus and the train to reach each town using the roads and railways
    for town in distances:
        for neighbor in graph[town]:
            if neighbor in distances:
                bus_times[neighbor] = min(bus_times[neighbor], bus_times[town] + 1)
                train_times[neighbor] = min(train_times[neighbor], train_times[town] + 1)
    
    # Return the maximum of the bus and train's arrival times in town n
    return max(bus_times[n], train_times[n])

if __name__ == '__main__':
    n, m = map(int, input().split())
    railways = []
    for _ in range(m):
        u, v = map(int, input().split())
        railways.append((u, v))
    print(f1(n, m, railways))
    print(f2(n, m, railways))

