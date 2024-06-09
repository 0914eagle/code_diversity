
def get_cyclic_permutations(n):
    # Initialize a list to store the cyclic permutations
    cyclic_permutations = []
    
    # Iterate over all possible permutations
    for permutation in itertools.permutations(range(1, n + 1)):
        # Convert the permutation to a list
        permutation_list = list(permutation)
        
        # Check if the permutation is cyclic
        if is_cyclic(permutation_list):
            # Add the cyclic permutation to the list
            cyclic_permutations.append(permutation_list)
    
    # Return the number of cyclic permutations modulo 10^9 + 7
    return len(cyclic_permutations) % (10**9 + 7)

def is_cyclic(permutation):
    # Initialize a set to store the nodes in the cycle
    cycle_set = set()
    
    # Initialize a variable to store the current node
    current_node = permutation[0]
    
    # Iterate until the cycle is complete
    while current_node not in cycle_set:
        # Add the current node to the cycle set
        cycle_set.add(current_node)
        
        # Get the next node in the cycle
        current_node = permutation[current_node - 1]
    
    # Return True if the cycle is complete, False otherwise
    return len(cycle_set) == len(permutation)

if __name__ == '__main__':
    n = int(input())
    print(get_cyclic_permutations(n))

