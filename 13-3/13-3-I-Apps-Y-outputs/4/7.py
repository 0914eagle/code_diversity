
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
            mst += graph[node]
            queue += graph[node]

    # Add the remaining edges to the MST
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j] and not graph[i][j] and not visited[i] and not visited[j]:
                mst.append(j)
                visited[j] = True
                queue.append(j)
                break

    return mst

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if is_possible(n, a):
            print("YES")
            mst = solve(n, a)
            for i in range(n-1):
                print(mst[i], mst[i+1])
        else:
            print("NO")

if __name__ == '__main__':
    main()

