
def f1(n):
    # Calculate the number of cyclic permutations of length n
    num_cyclic_permutations = 0
    
    # Iterate over all possible permutations of length n
    for p in itertools.permutations(range(1, n+1)):
        # Build the graph using the permutation p
        graph = f2(p)
        
        # Check if the graph has a simple cycle
        if has_simple_cycle(graph):
            num_cyclic_permutations += 1
    
    return num_cyclic_permutations % 1000000007

def f2(p):
    # Build the graph using the permutation p
    graph = {}
    for i in range(len(p)):
        # Find the largest j such that j < i and p[j] > p[i]
        j = max([j for j in range(i) if p[j] > p[i]])
        if j != -1:
            graph[i] = j
    
    # Find the smallest j such that i < j <= n and p[j] > p[i]
    j = min([j for j in range(i+1, len(p)) if p[j] > p[i]])
    if j != len(p):
        graph[i] = j
    
    return graph

def has_simple_cycle(graph):
    # Check if the graph has a simple cycle
    visited = set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited):
                return True
    return False

def has_cycle(graph, node, visited):
    # Check if the graph has a simple cycle starting from node
    if node in visited:
        return True
    visited.add(node)
    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visited):
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

