
def read_input():
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, k, times, edges

def dfs(node, visited, time):
    visited.add(node)
    for neighbor in edges[node - 1]:
        if neighbor not in visited:
            time = dfs(neighbor, visited, time)
    return min(time, times[node - 1])

def solve(n, k, times, edges):
    visited = set()
    time = float('inf')
    for i in range(1, n + 1):
        if i not in visited:
            time = min(time, dfs(i, visited, time))
    return time

def main():
    n, k, times, edges = read_input()
    print(solve(n, k, times, edges))

if __name__ == '__main__':
    main()

