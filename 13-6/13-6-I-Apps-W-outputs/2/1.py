
import itertools

def get_adjacency_list(n, edges):
    adjacency_list = [[] for _ in range(n)]
    for u, v in edges:
        adjacency_list[u - 1].append(v - 1)
        adjacency_list[v - 1].append(u - 1)
    return adjacency_list

def get_expected_length(n, edges):
    adjacency_list = get_adjacency_list(n, edges)
    visited = set([0])
    queue = [0]
    length = 0
    while queue:
        node = queue.pop(0)
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                length += 1
    return length / (n - 1)

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_expected_length(n, edges))

if __name__ == '__main__':
    main()

