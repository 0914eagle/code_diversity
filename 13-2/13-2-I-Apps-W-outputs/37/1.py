
def get_frequencies(n, edges):
    # Initialize a dictionary to map each node to its frequencies
    frequencies = {i: set() for i in range(1, n + 1)}
    
    # Iterate over the edges and add the frequencies to the corresponding nodes
    for i, j in edges:
        frequencies[i].add(i)
        frequencies[j].add(j)
    
    # Initialize the maximum number of frequencies used
    max_frequencies = 0
    
    # Iterate over the nodes and their frequencies
    for node, freqs in frequencies.items():
        # If the node has more than one frequency, add it to the maximum number of frequencies used
        if len(freqs) > 1:
            max_frequencies += 1
    
    # Return the maximum number of frequencies used
    return max_frequencies

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    print(get_frequencies(n, edges))

if __name__ == '__main__':
    main()

