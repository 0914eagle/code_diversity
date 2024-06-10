
def get_message_plan(n, a):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]
    
    # Add edges to the graph based on the input
    for i in range(n):
        for j in range(n):
            if i != j and a[i] > 0 and a[j] > 0:
                graph[i].append(j)
    
    # Breadth-first search to find a path from Polycarp (vertex 0) to all other vertices
    visited = [False] * n
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
    
    # If all vertices are reachable from Polycarp, return a plan
    if all(visited):
        plan = []
        for i in range(n):
            for j in graph[i]:
                if visited[i] and visited[j]:
                    plan.append((i, j))
        return plan
    else:
        return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    plan = get_message_plan(n, a)
    if plan == -1:
        print(-1)
    else:
        print(len(plan))
        for i, j in plan:
            print(i, j)

if __name__ == '__main__':
    main()

