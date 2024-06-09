
def get_cycles(permutation):
    # Initialize variables
    cycles = []
    visited = set()
    current = 0
    
    # Walk through the permutation
    while current not in visited:
        # Add the current position to the visited set
        visited.add(current)
        # Get the next position in the cycle
        next_pos = permutation[current] - 1
        # Add the current position to the current cycle
        cycles[-1].append(current + 1)
        # Update the current position
        current = next_pos
        
        # If we have visited all positions, add the final cycle
        if len(visited) == len(permutation):
            cycles.append([])
    
    # Return the cycles
    return cycles

def main():
    # Read the input
    N = int(input())
    permutation = [int(i) for i in input().split()]
    
    # Get the cycles
    cycles = get_cycles(permutation)
    
    # Print the output
    print(len(cycles))
    for cycle in cycles:
        print(*cycle)

if __name__ == '__main__':
    main()

