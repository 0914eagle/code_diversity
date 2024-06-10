
def get_min_paths(k_arr):
    # Initialize a dictionary to store the minimum paths from each fragment to the assembly node
    min_paths = {}
    
    # Iterate over the fragments
    for i, k in enumerate(k_arr):
        # Initialize the minimum path length to infinity
        min_path_len = float('inf')
        
        # Iterate over the factors of the current fragment's node number
        for factor in range(1, k + 1):
            # If the factor is not a prime number, continue to the next iteration
            if k % factor != 0:
                continue
            
            # If the factor is a prime number, calculate the distance from the current fragment to the assembly node
            distance = k // factor
            
            # If the distance is less than the minimum path length, update the minimum path length
            if distance < min_path_len:
                min_path_len = distance
        
        # Add the minimum path length for the current fragment to the dictionary
        min_paths[i] = min_path_len
    
    # Return the sum of the minimum paths for all fragments
    return sum(min_paths.values())

def main():
    # Read the number of fragments and their node numbers from stdin
    n = int(input())
    k_arr = list(map(int, input().split()))
    
    # Call the get_min_paths function and print the result
    print(get_min_paths(k_arr))

if __name__ == '__main__':
    main()

