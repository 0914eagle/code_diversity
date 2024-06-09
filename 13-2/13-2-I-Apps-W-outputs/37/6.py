
def get_frequencies(n, edges):
    # Initialize a dictionary to map each node to its frequency
    frequencies = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and assign frequencies to the nodes
    for i, j in edges:
        # If the frequencies of the two nodes are not already assigned, assign them the same frequency
        if frequencies[i] == 0 and frequencies[j] == 0:
            frequencies[i] = frequencies[j] = 1
        # If one of the frequencies is already assigned, assign the other node the complementary frequency
        elif frequencies[i] == 0:
            frequencies[i] = 1 - frequencies[j]
        elif frequencies[j] == 0:
            frequencies[j] = 1 - frequencies[i]
    
    # Return the frequencies of the nodes
    return [frequencies[i] for i in range(1, n + 1)]

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    frequencies = get_frequencies(n, edges)
    for freq in frequencies:
        print(freq)

if __name__ == '__main__':
    main()

