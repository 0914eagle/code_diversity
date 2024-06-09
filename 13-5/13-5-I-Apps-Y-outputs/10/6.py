
def get_input():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    return n, edges

def find_maximum_spanning_tree(n, edges):
    # Create a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)
    
    # Find the maximum spanning tree using Kruskal's algorithm
    mst = []
    visited = [False] * n
    def dfs(node, parent):
        nonlocal mst
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor != parent and not visited[neighbor]:
                dfs(neighbor, node)
                mst.append((node, neighbor))
    
    dfs(0, -1)
    return mst

def find_maximum_number_of_edges(n, edges):
    # Find the maximum spanning tree
    mst = find_maximum_spanning_tree(n, edges)
    
    # Count the number of edges in the MST
    num_edges = 0
    for edge in mst:
        num_edges += 1
    
    return num_edges

def find_vertices(n, edges, num_edges):
    # Find the maximum spanning tree
    mst = find_maximum_spanning_tree(n, edges)
    
    # Find the three vertices with the maximum number of edges
    vertices = []
    for i in range(n):
        if len(mst) == num_edges:
            break
        vertices.append(i)
        for edge in mst:
            if edge[0] == i or edge[1] == i:
                mst.remove(edge)
    
    return vertices

def main():
    n, edges = get_input()
    num_edges = find_maximum_number_of_edges(n, edges)
    vertices = find_vertices(n, edges, num_edges)
    print(num_edges)
    print(" ".join(map(str, vertices)))

if __name__ == '__main__':
    main()

