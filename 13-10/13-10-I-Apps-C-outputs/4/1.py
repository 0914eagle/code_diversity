
import sys

def get_boulder_graph(n_boulders, n_logs):
    graph = {}
    for i in range(n_boulders):
        graph[i] = set()
    for i in range(n_logs):
        log = input().split()
        graph[int(log[0])].add(int(log[1]))
        graph[int(log[1])].add(int(log[0]))
    return graph

def bfs(graph, start):
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, time = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, time + 1))
    return time

def get_min_time(n_people, n_boulders, n_logs):
    graph = get_boulder_graph(n_boulders, n_logs)
    time = 0
    for i in range(n_people):
        time += bfs(graph, i)
    return time

def main():
    n_people, n_boulders, n_logs = map(int, input().split())
    print(get_min_time(n_people, n_boulders, n_logs))

if __name__ == '__main__':
    main()

