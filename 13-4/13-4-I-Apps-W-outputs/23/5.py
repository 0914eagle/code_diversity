
def is_possible(a, b):
    
    # Initialize the graph with the given edges
    graph = {}
    for i in range(len(a)):
        graph[i+1] = [a[i], b[i]]

    # Breadth-first search to find a path from the initial values to the desired values
    queue = [(1, [])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex == len(a):
            return True
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            queue.append((neighbor, path + [vertex]))
    return False

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(m):
        c, d = map(int, input().split())
        graph[c] = [d]
        graph[d] = [c]
    print("Yes") if is_possible(a, b) else print("No")

if __name__ == '__main__':
    main()

