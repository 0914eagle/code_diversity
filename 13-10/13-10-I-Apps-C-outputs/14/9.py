
def get_independent_set_size(n, m):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    # Initialize a set to store the vertices in the independent set
    independent_set = set()
    
    # Recursively find the maximum independent set
    find_maximum_independent_set(graph, independent_set, 0)
    
    # Return the size of the maximum independent set
    return len(independent_set)

def find_maximum_independent_set(graph, independent_set, vertex):
    # Base case: all vertices have been visited
    if vertex == len(graph):
        return
    
    # Recursive case: visit the current vertex and its neighbors
    for neighbor in graph[vertex]:
        if neighbor not in independent_set:
            independent_set.add(neighbor)
            find_maximum_independent_set(graph, independent_set, neighbor)
    
    # Backtrack: remove the current vertex from the independent set if it is not in the maximum independent set
    if vertex not in independent_set:
        independent_set.add(vertex)
        find_maximum_independent_set(graph, independent_set, vertex+1)
        independent_set.remove(vertex)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_independent_set_size(n, m))

