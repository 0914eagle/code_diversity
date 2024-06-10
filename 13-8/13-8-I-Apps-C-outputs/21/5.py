
def get_path_lengths(k_list):
    # Initialize a dictionary to store the path lengths from each fragment to the assembly node
    path_lengths = {}
    
    # Iterate over the fragments
    for i, k in enumerate(k_list):
        # Initialize the path length for this fragment as 0
        path_length = 0
        
        # Iterate over the nodes in the system
        for node in range(1, k+1):
            # If the current node is a factorial of the current fragment's node, add the path length to the total
            if node == k!:
                path_length += 1
        
        # Add the path length for this fragment to the dictionary
        path_lengths[i] = path_length
    
    return path_lengths

def get_min_path_length(path_lengths):
    # Initialize the minimum path length as infinity
    min_path_length = float('inf')
    
    # Iterate over the path lengths
    for path_length in path_lengths.values():
        # If the current path length is less than the minimum path length, update the minimum path length
        if path_length < min_path_length:
            min_path_length = path_length
    
    return min_path_length

def main():
    # Read the number of fragments and the nodes where the fragments are located from stdin
    n = int(input())
    k_list = [int(input()) for _ in range(n)]
    
    # Get the path lengths from each fragment to the assembly node
    path_lengths = get_path_lengths(k_list)
    
    # Get the minimum path length
    min_path_length = get_min_path_length(path_lengths)
    
    # Print the minimum path length
    print(min_path_length)

if __name__ == '__main__':
    main()

