
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def is_possible(n, a):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n + 1)]
    
    # Add edges to the graph
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and a[i - 1] >= j - 1:
                graph[i].append(j)
    
    # Check if the graph is connected
    visited = [False] * (n + 1)
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            queue += graph[vertex]
    
    return visited[n]

def get_plan(n, a):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n + 1)]
    
    # Add edges to the graph
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and a[i - 1] >= j - 1:
                graph[i].append(j)
    
    # Breadth-first search to find a plan
    visited = [False] * (n + 1)
    queue = [(1, [])]
    while queue:
        (vertex, path) = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if neighbor not in path:
                    queue.append((neighbor, path + [vertex]))
                    if neighbor == n:
                        return path
    
    return []

def main():
    n, a = get_input()
    if is_possible(n, a):
        plan = get_plan(n, a)
        print(len(plan))
        for i in range(len(plan) - 1):
            print(plan[i], plan[i + 1])
    else:
        print(-1)

if __name__ == '__main__':
    main()

