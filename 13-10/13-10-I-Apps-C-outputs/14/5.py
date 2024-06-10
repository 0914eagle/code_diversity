
def find_maximum_independent_set(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize a set to store the independent set
    independent_set = set()
    
    # Iterate through the graph and find an independent set
    for node in graph:
        if node not in independent_set:
            independent_set.add(node)
            for neighbor in graph[node]:
                if neighbor in independent_set:
                    independent_set.remove(neighbor)
    
    return len(independent_set)

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    print(find_maximum_independent_set(n, edges))

if __name__ == '__main__':
    main()

