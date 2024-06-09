
def f1(n):
    # calculate the number of cyclic permutations
    num_cyclic_permutations = 0
    
    # iterate over all permutations of length n
    for p in permutations(range(1, n+1)):
        # build the graph using the permutation p
        graph = build_graph(p)
        
        # check if the graph has a simple cycle
        if has_simple_cycle(graph):
            num_cyclic_permutations += 1
    
    return num_cyclic_permutations % (10**9 + 7)

def build_graph(p):
    # initialize an empty graph with n nodes
    graph = [[] for _ in range(len(p))]
    
    # iterate over all nodes in the permutation
    for i in range(len(p)):
        # find the largest j such that j < i and p[j] > p[i]
        j = max([j for j in range(i) if p[j] > p[i]])
        
        # if such a j exists, add an edge between node i and node j
        if j != -1:
            graph[i].append(j)
        
        # find the smallest j such that i < j <= n and p[j] > p[i]
        j = min([j for j in range(i+1, len(p)) if p[j] > p[i]])
        
        # if such a j exists, add an edge between node i and node j
        if j != -1:
            graph[i].append(j)
    
    return graph

def has_simple_cycle(graph):
    # initialize a set to keep track of visited nodes
    visited = set()
    
    # iterate over all nodes in the graph
    for node in range(len(graph)):
        # if the node has not been visited, start a DFS from it
        if node not in visited:
            if dfs(graph, node, visited):
                return True
    
    return False

def dfs(graph, node, visited):
    # mark the current node as visited
    visited.add(node)
    
    # iterate over all neighbors of the current node
    for neighbor in graph[node]:
        # if the neighbor has not been visited, recurse on it
        if neighbor not in visited:
            if dfs(graph, neighbor, visited):
                return True
    
    # if we reach this point, all neighbors have been visited
    # so we can remove the current node from the visited set
    visited.remove(node)
    return False

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

