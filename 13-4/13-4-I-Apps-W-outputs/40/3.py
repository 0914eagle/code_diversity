
def f1(n):
    # calculate the number of cyclic permutations
    num_cyclic_permutations = 0
    
    # iterate over all possible permutations
    for permutation in itertools.permutations(range(1, n+1)):
        # build the graph using the permutation
        graph = f2(permutation)
        
        # check if the graph has a simple cycle
        if has_simple_cycle(graph):
            num_cyclic_permutations += 1
    
    return num_cyclic_permutations % 1000000007

def f2(permutation):
    # build the graph using the permutation
    graph = {}
    for i in range(len(permutation)):
        # find the largest j such that j < i and p[j] > p[i]
        j = max([j for j in range(i) if permutation[j] > permutation[i]])
        if j != -1:
            graph[i] = j
    
    # find the smallest j such that i < j <= n and p[j] > p[i]
    for i in range(len(permutation)):
        j = min([j for j in range(i+1, len(permutation)+1) if permutation[j-1] > permutation[i]])
        if j != len(permutation)+1:
            graph[i] = j
    
    return graph

def has_simple_cycle(graph):
    # check if the graph has a simple cycle
    visited = set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited):
                return True
    return False

def has_cycle(graph, node, visited):
    # check if the graph has a simple cycle starting from the given node
    if node in visited:
        return True
    
    visited.add(node)
    if node in graph:
        return has_cycle(graph, graph[node], visited)
    return False

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

