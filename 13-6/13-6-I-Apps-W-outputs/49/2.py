
def get_cycles(permutation):
    # Initialize a set to store the cycles
    cycles = set()
    
    # Iterate through the permutation
    for i in range(len(permutation)):
        # If the current position has not been visited before, start a new cycle
        if i not in cycles:
            # Start a new cycle by visiting the current position
            cycle = [i]
            # Visit the next position in the cycle
            j = permutation[i]
            # While the current position has not been visited before, continue visiting positions in the cycle
            while j not in cycles:
                # Add the current position to the cycle
                cycle.append(j)
                # Visit the next position in the cycle
                j = permutation[j]
            # Add the cycle to the set of cycles
            cycles.add(tuple(cycle))
    
    # Return the set of cycles
    return cycles

def main():
    # Read the input permutation
    N = int(input())
    permutation = list(map(int, input().split()))
    
    # Get the cycles in the permutation
    cycles = get_cycles(permutation)
    
    # Print the number of cycles
    print(len(cycles))
    # Print the cycles
    for cycle in cycles:
        print(*cycle)

if __name__ == '__main__':
    main()

