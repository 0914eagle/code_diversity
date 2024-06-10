
import math

def get_neighbors(graph, node):
    neighbors = []
    for i in range(len(graph)):
        if node in graph[i]:
            neighbors.append(i)
    return neighbors

def get_paths(graph, walk):
    paths = []
    current_path = []
    for node in walk:
        neighbors = get_neighbors(graph, node)
        for neighbor in neighbors:
            if neighbor not in current_path:
                current_path.append(neighbor)
                paths.append(current_path)
                current_path = []
    return paths

def get_chance(graph, walk):
    paths = get_paths(graph, walk)
    total_paths = math.factorial(len(graph))
    unique_paths = len(set(map(tuple, paths)))
    return unique_paths / total_paths

def main():
    nodes, rooms, walk = [int(i) for i in input().split()]
    graph = [set() for _ in range(nodes)]
    for i in range(rooms):
        node = int(input())
        graph[node].add(i)
    chance = get_chance(graph, walk)
    print(chance)

if __name__ == '__main__':
    main()

