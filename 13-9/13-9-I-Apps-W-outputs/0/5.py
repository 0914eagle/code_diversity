
def dfs(start, visited, graph):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

def get_grade(times, k):
    n = len(times)
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(1, n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    dfs(1, visited, graph)
    return sum(times[:k])

def main():
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    print(get_grade(times, k))

if __name__ == '__main__':
    main()

