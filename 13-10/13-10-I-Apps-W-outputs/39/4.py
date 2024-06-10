
def find_path(tree, x, y, a, b, k):
    # Add the edge between x and y to the tree
    tree.add_edge(x, y)
    # Check if there is a path from a to b with k edges
    path = bfs(tree, a, b, k)
    # Remove the edge between x and y from the tree
    tree.remove_edge(x, y)
    return "YES" if path else "NO"

def bfs(tree, start, end, k):
    # Initialize a queue and a visited set
    queue = [start]
    visited = set()
    # Loop until the queue is empty
    while queue:
        # Get the first vertex from the queue
        vertex = queue.pop(0)
        # If the vertex is the end vertex, return the path
        if vertex == end:
            return [vertex]
        # If the vertex has not been visited, mark it as visited and add its neighbors to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += tree.neighbors(vertex)
    # If the queue is empty and the end vertex has not been visited, there is no path from start to end with k edges
    return None

def main():
    # Read the input
    n, m = map(int, input().split())
    tree = Graph(n)
    for _ in range(m):
        x, y = map(int, input().split())
        tree.add_edge(x, y)
    q = int(input())
    for _ in range(q):
        x, y, a, b, k = map(int, input().split())
        print(find_path(tree, x, y, a, b, k))

if __name__ == '__main__':
    main()

