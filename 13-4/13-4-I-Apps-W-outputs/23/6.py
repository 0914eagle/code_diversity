
def is_possible(a, b):
    
    # Initialize the graph with the given edges
    graph = {}
    for i in range(len(a)):
        graph[i+1] = [a[i], b[i]]
    
    # Breadth-first search to find a path from the initial values to the target values
    queue = [(1, [])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node == len(a):
            return True
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, path + [node]))
    
    return False

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(m):
        c, d = map(int, input().split())
        graph[c] = [d]
    
    print("Yes") if is_possible(a, b) else print("No")

if __name__ == '__main__':
    main()

