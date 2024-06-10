
def get_paths(n, k_list):
    # Initialize a dictionary to store the distances from each fragment to the assembly node
    distances = {}
    
    # Loop through each fragment
    for i in range(n):
        # Initialize the distance from the current fragment to the assembly node as infinity
        distance = float('inf')
        
        # Loop through each node in the network
        for node in range(1, n+1):
            # If the current fragment is located at the current node, set the distance to 0
            if node == k_list[i]:
                distance = 0
                break
            # If the current node is connected to the current fragment, update the distance
            elif node % (k_list[i] * k_list[i]) == 0:
                distance = min(distance, node // (k_list[i] * k_list[i]))
        
        # Add the distance from the current fragment to the assembly node to the dictionary
        distances[i] = distance
    
    # Return the sum of the distances from all fragments to the assembly node
    return sum(distances.values())

def main():
    # Read the number of fragments and the locations of the fragments from stdin
    n = int(input())
    k_list = [int(x) for x in input().split()]
    
    # Call the get_paths function to get the sum of the distances from all fragments to the assembly node
    print(get_paths(n, k_list))

if __name__ == '__main__':
    main()

