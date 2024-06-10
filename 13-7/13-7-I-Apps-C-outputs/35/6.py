
import sys

def get_input():
    return list(map(int, sys.stdin.readline().strip().split()))

def get_graph(N, edges):
    graph = [[] for _ in range(N + 1)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    return graph

def get_distances(graph, start):
    distances = [float('inf')] * (len(graph) + 1)
    distances[start] = 0
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances

def get_pairs(distances, N):
    pairs = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if distances[i] + distances[j] == N - 1:
                pairs.append((i, j))
    return pairs

def count_ways(pairs, N):
    count = 0
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if pairs[i][0] in pairs[j] or pairs[i][1] in pairs[j]:
                count += 1
    return count % (10**9 + 7)

def main():
    N = get_input()[0]
    edges = [(x, y) for x, y in zip(get_input(), get_input())]
    graph = get_graph(N, edges)
    distances = get_distances(graph, 1)
    pairs = get_pairs(distances, N)
    print(count_ways(pairs, N))

if __name__ == '__main__':
    main()

