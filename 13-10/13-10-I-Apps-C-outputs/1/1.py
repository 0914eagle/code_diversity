
import sys

def dijkstra(graph, start, destination):
    visited = set()
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == destination:
                return dist
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (dist + weight, neighbor))
    return -1

def get_shortest_paths(graph, start, destination):
    visited = set()
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == destination:
                return dist
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (dist + weight, neighbor))
    return -1

def get_shortest_paths_count(graph, start, destination):
    visited = set()
    queue = [(0, start)]
    count = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == destination:
                return count
            for neighbor, weight in graph[node].items():
                heapq.heappush(queue, (dist + weight, neighbor))
                count += 1
    return -1

def main():
    graph = {}
    for _ in range(int(input())):
        origin, destination, length = map(int, input().split())
        if origin not in graph:
            graph[origin] = {}
        if destination not in graph:
            graph[destination] = {}
        graph[origin][destination] = length
        graph[destination][origin] = length

    for road in graph:
        print(get_shortest_paths_count(graph, road, road))

if __name__ == '__main__':
    main()

