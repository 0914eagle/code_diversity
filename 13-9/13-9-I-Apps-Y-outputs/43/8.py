
def solve(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]
    # Add edges to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)
    # Check if the graph is connected
    visited = [False] * n
    queue = [0]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            queue += graph[node]
    if not all(visited):
        return "NO"
    # Find a valid assignment of roads
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j] and [i, j] not in roads:
                roads.append([i, j])
    if len(roads) == n-1:
        return "YES\n" + "\n".join([f"{i} {j}" for i, j in roads])
    else:
        return "NO"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))

if __name__ == '__main__':
    main()

