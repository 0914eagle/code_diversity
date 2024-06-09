
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
    # Initialize a set to store the nodes that have been visited
    visited = set()
    
    # Initialize a variable to store the current node
    current_node = permutation[0]
    
    # Iterate until the current node is the first node
    while current_node != permutation[0]:
        # Add the current node to the visited set
        visited.add(current_node)
        
        # Find the next node in the cycle
        next_node = permutation[current_node - 1]
        
        # Check if the next node has been visited before
        if next_node in visited:
            # Return True if the next node has been visited before
            return True
        
        # Set the current node to the next node
        current_node = next_node
    
    # Return False if the permutation is not cyclic
    return False

if __name__ == '__main__':
    n = int(input())
    print(get_cyclic_permutations(n))

