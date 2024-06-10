
def get_min_path_length(fragments, assembly_node):
    # Initialize a dictionary to store the shortest path length from each fragment to the assembly node
    shortest_path_lengths = {}
    
    # Loop through each fragment
    for fragment in fragments:
        # Initialize the shortest path length for this fragment to infinity
        shortest_path_length = float('inf')
        
        # Loop through each node in the system
        for node in range(1, len(fragments) + 1):
            # If the current node is the fragment or the assembly node, skip it
            if node == fragment or node == assembly_node:
                continue
            
            # If the current node is not the fragment or the assembly node, calculate the distance between the current node and the fragment
            distance = abs(fragment - node)
            
            # If the distance is less than the current shortest path length, update the shortest path length
            if distance < shortest_path_length:
                shortest_path_length = distance
        
        # Add the shortest path length for this fragment to the dictionary
        shortest_path_lengths[fragment] = shortest_path_length
    
    # Return the sum of the shortest path lengths for all fragments
    return sum(shortest_path_lengths.values())

def main():
    # Read the number of fragments and the locations of the fragments from stdin
    num_fragments = int(input())
    fragments = list(map(int, input().split()))
    
    # Determine the assembly node
    assembly_node = 1
    
    # Calculate the minimum path length from each fragment to the assembly node
    min_path_length = get_min_path_length(fragments, assembly_node)
    
    # Print the minimum path length
    print(min_path_length)

if __name__ == '__main__':
    main()

