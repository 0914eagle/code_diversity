
import sys
import math

sys.setrecursionlimit(10**6)

def shortest_path(graph, start, end, visited):
    if start == end:
        return 0
    
    visited.add(start)
    shortest_path = math.inf
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = shortest_path(graph, neighbor, end, visited)
            if path < shortest_path:
                shortest_path = path
    
    return shortest_path + 1

def find_danger_level(graph):
    danger_level = []
    
    for i in range(1, len(graph) + 1):
        visited = set()
        danger_level.append(shortest_path(graph, i, len(graph), visited))
    
    return danger_level

def main():
    num_chambers, num_tunnels = map(int, input().split())
    graph = [[] for _ in range(num_chambers + 1)]
    
    for _ in range(num_tunnels):
        a, b, length = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    danger_level = find_danger_level(graph)
    print(*[d % (10**9 + 7) for d in danger_level])

if __name__ == "__main__":
    main()

