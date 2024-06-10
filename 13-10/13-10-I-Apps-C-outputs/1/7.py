
import sys

def dijkstra(graph, start, end):
    visited = set()
    queue = [[start, 0]]
    while queue:
        (node, cost) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end:
                return cost
            for neighbor, weight in graph[node].items():
                queue.append([neighbor, cost + weight])
    return float('inf')

def find_shortest_paths(graph, start, end):
    visited = set()
    queue = [[start, 0]]
    while queue:
        (node, cost) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end:
                return cost
            for neighbor, weight in graph[node].items():
                queue.append([neighbor, cost + weight])
    return float('inf')

def number_of_shortest_paths(graph, start, end):
    visited = set()
    queue = [[start, 0]]
    count = 0
    while queue:
        (node, cost) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end:
                count += 1
            for neighbor, weight in graph[node].items():
                queue.append([neighbor, cost + weight])
    return count

def main():
    num_cities, num_roads = map(int, input().split())
    graph = {}
    for _ in range(num_roads):
        city1, city2, length = map(int, input().split())
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}
        graph[city1][city2] = length
        graph[city2][city1] = length
    for road in range(num_roads):
        city1, city2, length = map(int, input().split())
        print(number_of_shortest_paths(graph, city1, city2))

if __name__ == '__main__':
    main()

