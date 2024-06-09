
def get_min_instability(towers, k):
    # Initialize the minimum instability and the number of operations
    min_instability = float('inf')
    num_operations = 0
    
    # Loop through all possible combinations of towers
    for i in range(len(towers)):
        for j in range(i+1, len(towers)):
            # Check if the operation is valid (i.e., i != j)
            if i != j:
                # Perform the operation and calculate the new instability
                new_instability = abs(towers[i] - towers[j])
                
                # Check if the new instability is lower than the current minimum
                if new_instability < min_instability:
                    min_instability = new_instability
                    num_operations = 1
                # Check if the new instability is equal to the current minimum
                elif new_instability == min_instability:
                    num_operations += 1
    
    # Return the minimum instability and the number of operations
    return min_instability, num_operations

def get_operations(towers, k):
    # Initialize the list of operations
    operations = []
    
    # Loop through all possible combinations of towers
    for i in range(len(towers)):
        for j in range(i+1, len(towers)):
            # Check if the operation is valid (i.e., i != j)
            if i != j:
                # Perform the operation and calculate the new instability
                new_instability = abs(towers[i] - towers[j])
                
                # Check if the new instability is lower than the current minimum
                if new_instability < min_instability:
                    min_instability = new_instability
                    operations = [(i, j)]
                # Check if the new instability is equal to the current minimum
                elif new_instability == min_instability:
                    operations.append((i, j))
    
    # Return the list of operations
    return operations

def main():
    # Read the input data
    n, k = map(int, input().split())
    towers = list(map(int, input().split()))
    
    # Calculate the minimum instability and the number of operations
    min_instability, num_operations = get_min_instability(towers, k)
    
    # Print the output
    print(min_instability, num_operations)
    for i, j in get_operations(towers, k):
        print(i, j)

if __name__ == '__main__':
    main()

