
def f1(n, edges):
    # Calculate the number of possible pairs
    num_pairs = n / 2
    
    # Initialize a dictionary to store the number of edges for each pair
    pairs = {i: 0 for i in range(1, num_pairs + 1)}
    
    # Iterate over the edges and increment the number of edges for each pair
    for edge in edges:
        pairs[edge[0]] += 1
        pairs[edge[1]] += 1
    
    # Initialize a set to store the pairs that have at least one edge
    valid_pairs = set()
    
    # Iterate over the pairs and check if they have at least one edge
    for pair, num_edges in pairs.items():
        if num_edges > 0:
            valid_pairs.add(pair)
    
    # Return the number of valid pairs modulo 10^9 + 7
    return len(valid_pairs) % (10**9 + 7)

def f2(n, edges):
    # Calculate the number of possible pairs
    num_pairs = n / 2
    
    # Initialize a dictionary to store the number of edges for each pair
    pairs = {i: 0 for i in range(1, num_pairs + 1)}
    
    # Iterate over the edges and increment the number of edges for each pair
    for edge in edges:
        pairs[edge[0]] += 1
        pairs[edge[1]] += 1
    
    # Initialize a set to store the pairs that have at least one edge
    valid_pairs = set()
    
    # Iterate over the pairs and check if they have at least one edge
    for pair, num_edges in pairs.items():
        if num_edges > 0:
            valid_pairs.add(pair)
    
    # Return the number of valid pairs modulo 10^9 + 7
    return len(valid_pairs) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(f1(n, edges))
    print(f2(n, edges))

