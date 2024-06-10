
def get_shortest_paths(n, m, roads):
    # Initialize a dictionary to store the shortest paths from each city to all other cities
    shortest_paths = {}
    for i in range(n):
        shortest_paths[i] = {i: 0}
    
    # Loop through each road and update the shortest paths between the two cities
    for o, d, l in roads:
        if o not in shortest_paths:
            shortest_paths[o] = {d: l}
        else:
            shortest_paths[o][d] = l
    
    # Loop through each city and find the shortest path from that city to all other cities
    for city in range(n):
        for other_city in range(n):
            if city != other_city:
                shortest_path = float('inf')
                for road in shortest_paths[city]:
                    if road != other_city and shortest_paths[city][road] + shortest_paths[road][other_city] < shortest_path:
                        shortest_path = shortest_paths[city][road] + shortest_paths[road][other_city]
                shortest_paths[city][other_city] = shortest_path
    
    # Return the number of shortest paths containing each road
    result = []
    for o, d, l in roads:
        result.append(shortest_paths[o][d])
    return result

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        o, d, l = map(int, input().split())
        roads.append((o, d, l))
    result = get_shortest_paths(n, m, roads)
    for r in result:
        print(r)

if __name__ == '__main__':
    main()

