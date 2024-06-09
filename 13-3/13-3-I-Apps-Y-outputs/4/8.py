
def is_possible(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)

    # Check if all nodes are reachable from each other
    visited = [False] * n
    queue = [0]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            queue += graph[node]

    # Check if all pairs of directly connected districts belong to different gangs
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j] and graph[i][j]:
                return False

    return True

def solve(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)

    # Find a minimum spanning tree
    mst = []
    visited = [False] * n
    queue = [0]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            mst.append(node)
            queue += graph[node]

    # Add edges to form a complete graph
    for i in range(n):
        for j in range(i+1, n):
            if not graph[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    # Find a Eulerian circuit
    circuit = []
    visited = [False] * n
    queue = [0]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            circuit.append(node)
            queue += graph[node]

    # Return the solution
    return circuit

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if is_possible(n, a):
            print("YES")
            print(*solve(n, a))
        else:
            print("NO")

