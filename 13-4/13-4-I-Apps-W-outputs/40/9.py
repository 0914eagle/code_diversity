
def get_cyclic_permutations(n):
    # Initialize a list to store the cyclic permutations
    cyclic_permutations = []
    
    # Iterate over all possible permutations
    for permutation in permutations(range(1, n + 1)):
        # Convert the permutation to a graph
        graph = convert_to_graph(permutation)
        
        # Check if the graph has a simple cycle
        if has_simple_cycle(graph):
            # Add the permutation to the list of cyclic permutations
            cyclic_permutations.append(permutation)
    
    # Return the number of cyclic permutations modulo 10^9 + 7
    return len(cyclic_permutations) % (10**9 + 7)

def permutations(n):
    # Yield all possible permutations of n elements
    if n == 1:
        yield [1]
    else:
        for i in range(1, n + 1):
            for permutation in permutations(n - 1):
                yield [i] + permutation

def convert_to_graph(permutation):
    # Initialize an empty graph with n nodes
    graph = [[] for _ in range(len(permutation))]
    
    # Add edges to the graph based on the permutation
    for i in range(len(permutation)):
        # Find the largest j such that j < i and p_j > p_i
        largest_j = find_largest_j(permutation, i)
        
        # Add an edge between node i and node j
        graph[i].append(largest_j)
        
        # Find the smallest j such that i < j <= n and p_j > p_i
        smallest_j = find_smallest_j(permutation, i)
        
        # Add an edge between node i and node j
        graph[i].append(smallest_j)
    
    return graph

def find_largest_j(permutation, i):
    # Find the largest j such that j < i and p_j > p_i
    for j in range(i - 1, -1, -1):
        if permutation[j] > permutation[i]:
            return j
    return -1

def find_smallest_j(permutation, i):
    # Find the smallest j such that i < j <= n and p_j > p_i
    for j in range(i + 1, len(permutation)):
        if permutation[j] > permutation[i]:
            return j
    return len(permutation)

def has_simple_cycle(graph):
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a queue to store the nodes to visit
    queue = [0]
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)
        
        # If the node has not been visited, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    
    # If all nodes have been visited, the graph has no simple cycle
    return len(visited) == len(graph)

if __name__ == '__main__':
    n = int(input())
    print(get_cyclic_permutations(n))

