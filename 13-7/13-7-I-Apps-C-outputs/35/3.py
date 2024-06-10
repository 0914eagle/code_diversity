
import sys

def get_input():
    N = int(input())
    edges = []
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def get_shortest_path(edges, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == end:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for neighbor in edges:
            if neighbor[0] == node:
                queue.append((neighbor[1], distance + 1))
    return -1

def count_ways(edges, N):
    pairs = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            pairs.append((i, j))
    count = 0
    for pair in pairs:
        has_ribbon = False
        for edge in edges:
            if edge[0] in pair and edge[1] in pair:
                has_ribbon = True
                break
        if has_ribbon:
            count += 1
    return count % (10**9 + 7)

def main():
    N, edges = get_input()
    print(count_ways(edges, N))

if __name__ == '__main__':
    main()

