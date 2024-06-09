
def get_min_instability(towers, k):
    # Initialize the minimum instability and the number of operations
    min_instability = float('inf')
    num_operations = 0
    
    # Loop through all possible sequences of operations
    for sequence in itertools.product(range(1, len(towers)), repeat=k):
        # Clone the list of towers
        tower_copy = towers[:]
        
        # Perform the operations in the sequence
        for i, j in sequence:
            tower_copy[j-1] += tower_copy[i-1]
            tower_copy[i-1] = 0
        
        # Calculate the instability of the current sequence
        instability = max(tower_copy) - min(tower_copy)
        
        # Update the minimum instability and the number of operations if necessary
        if instability < min_instability:
            min_instability = instability
            num_operations = k
    
    return min_instability, num_operations, sequence

def main():
    n, k = map(int, input().split())
    towers = list(map(int, input().split()))
    min_instability, num_operations, sequence = get_min_instability(towers, k)
    print(min_instability, num_operations)
    for i, j in sequence:
        print(i, j)

if __name__ == '__main__':
    main()

