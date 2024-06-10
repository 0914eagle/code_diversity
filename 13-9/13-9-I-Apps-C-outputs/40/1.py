
import math

def get_neighbors(graph, node):
    return graph[node]

def get_paths(graph, nodes):
    paths = []
    for node in nodes:
        neighbors = get_neighbors(graph, node)
        for neighbor in neighbors:
            paths.append([node, neighbor])
    return paths

def get_chance(graph, nodes, sentry_move_time):
    paths = get_paths(graph, nodes)
    total_paths = len(paths)
    sentry_visits = math.floor(sentry_move_time / len(nodes))
    captured_paths = 0
    for i in range(sentry_visits):
        sentry_path = paths[i]
        captured_paths += 1 if sentry_path[0] == sentry_path[1] else 0
    return 1 - captured_paths / total_paths

def main():
    nodes_count, walk_length = map(int, input().split())
    nodes = list(map(int, input().split()))
    graph = [[] for _ in range(nodes_count)]
    for i in range(nodes_count):
        neighbors_count = int(input())
        graph[i] = list(map(int, input().split()))
    sentry_move_time = int(input())
    chance = get_chance(graph, nodes, sentry_move_time)
    print(chance)

if __name__ == '__main__':
    main()

