
def get_min_wolves(V, P, edges, pigs):
    # Initialize a graph with V vertices and E edges
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a visited array and a parent array
    visited = [False] * V
    parent = [None] * V
    
    # Function to check if a pig can escape from a vertex
    def can_escape(v):
        if visited[v]:
            return False
        visited[v] = True
        for neighbor in graph[v]:
            if parent[neighbor] is None:
                parent[neighbor] = v
                if can_escape(neighbor):
                    return True
        return False
    
    # Function to remove a wolf from a vertex
    def remove_wolf(v):
        if visited[v]:
            return
        visited[v] = True
        for neighbor in graph[v]:
            if parent[neighbor] is None:
                parent[neighbor] = v
                remove_wolf(neighbor)
    
    # Initialize the number of wolves to remove
    num_wolves = 0
    
    # Iterate through the pigs and check if they can escape
    for pig in pigs:
        if not can_escape(pig):
            num_wolves += 1
    
    # Remove the wolves one by one and check if the pigs can escape
    for i in range(num_wolves):
        remove_wolf(pigs[i])
        if all(can_escape(pig) for pig in pigs):
            break
    
    return num_wolves

def main():
    V, P = map(int, input().split())
    edges = []
    for _ in range(V-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    pigs = list(map(int, input().split()))
    print(get_min_wolves(V, P, edges, pigs))

if __name__ == '__main__':
    main()

