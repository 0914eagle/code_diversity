
def count_simple_loops(num_stations, connections):
    def dfs(curr_station, start_station, visited, num_visited):
        if num_visited == num_stations and curr_station == start_station:
            return 1
        if visited[curr_station]:
            return 0
        visited[curr_station] = True
        count = 0
        for next_station in range(num_stations):
            if connections[curr_station][next_station]:
                count += dfs(next_station, start_station, visited, num_visited + 1)
        visited[curr_station] = False
        return count

    num_simple_loops = 0
    for start_station in range(num_stations):
        visited = [False] * num_stations
        num_simple_loops += dfs(start_station, start_station, visited, 1)
    
    return num_simple_loops

# Read input
num_stations = int(input())
num_connections = int(input())
connections = [[0] * num_stations for _ in range(num_stations)]
for _ in range(num_connections):
    s, t = map(int, input().split())
    connections[s][t] = 1

# Calculate and print output
print(count_simple_loops(num_stations, connections))
