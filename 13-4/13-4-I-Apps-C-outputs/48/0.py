
def f1(N, edges):
    # Calculate the number of pairs
    num_pairs = N // 2
    
    # Initialize a dictionary to store the pairs
    pairs = {}
    
    # Iterate over the edges
    for edge in edges:
        # Get the vertices of the edge
        u, v = edge
        
        # If the pair (u, v) is not in the dictionary, add it
        if (u, v) not in pairs:
            pairs[(u, v)] = 1
        # If the pair (v, u) is not in the dictionary, add it
        elif (v, u) not in pairs:
            pairs[(v, u)] = 1
        # If the pair is already in the dictionary, increment the count
        else:
            pairs[(u, v)] += 1
    
    # Initialize a counter for the number of pairs that satisfy the condition
    count = 0
    
    # Iterate over the pairs
    for pair in pairs:
        # If the count of the pair is equal to the number of pairs, increment the counter
        if pairs[pair] == num_pairs:
            count += 1
    
    # Return the count modulo 10^9 + 7
    return count % 1000000007

def f2(N, edges):
    # Calculate the number of pairs
    num_pairs = N // 2
    
    # Initialize a dictionary to store the pairs
    pairs = {}
    
    # Iterate over the edges
    for edge in edges:
        # Get the vertices of the edge
        u, v = edge
        
        # If the pair (u, v) is not in the dictionary, add it
        if (u, v) not in pairs:
            pairs[(u, v)] = 1
        # If the pair (v, u) is not in the dictionary, add it
        elif (v, u) not in pairs:
            pairs[(v, u)] = 1
        # If the pair is already in the dictionary, increment the count
        else:
            pairs[(u, v)] += 1
    
    # Initialize a counter for the number of pairs that satisfy the condition
    count = 0
    
    # Iterate over the pairs
    for pair in pairs:
        # If the count of the pair is equal to the number of pairs, increment the counter
        if pairs[pair] == num_pairs:
            count += 1
    
    # Return the count modulo 10^9 + 7
    return count % 1000000007

if __name__ == '__main__':
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f1(N, edges))
    print(f2(N, edges))

