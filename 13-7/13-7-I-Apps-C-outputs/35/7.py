
import sys
import itertools

def get_input():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def get_pairs(N, edges):
    pairs = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            pairs.append((i, j))
    return pairs

def get_shortest_path(N, edges, pairs):
    shortest_paths = []
    for i in range(N):
        shortest_paths.append([sys.maxsize] * (N + 1))
        shortest_paths[i][i] = 0
    for i in range(N - 1):
        x, y = edges[i]
        shortest_paths[x][y] = shortest_paths[y][x] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])
    return shortest_paths

def get_count(N, edges, pairs, shortest_paths):
    count = 0
    for pair in pairs:
        x, y = pair
        for i in range(N - 1):
            if shortest_paths[x][y] > shortest_paths[x][edges[i][0]] + shortest_paths[edges[i][1]][y]:
                break
        else:
            count += 1
    return count

def main():
    N, edges = get_input()
    pairs = get_pairs(N, edges)
    shortest_paths = get_shortest_path(N, edges, pairs)
    count = get_count(N, edges, pairs, shortest_paths)
    print(count % (10**9 + 7))

if __name__ == '__main__':
    main()

