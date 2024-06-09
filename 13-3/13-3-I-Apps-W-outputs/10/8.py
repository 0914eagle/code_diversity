
def get_min_instability(towers, k):
    # Initialize the minimum instability and the number of operations
    min_instability = float('inf')
    num_operations = 0
    
    # Loop through all possible combinations of towers
    for i in range(len(towers)):
        for j in range(i+1, len(towers)):
            # Check if the instability of the combination is less than the current minimum
            instability = abs(towers[i] - towers[j])
            if instability < min_instability:
                # Update the minimum instability and the number of operations
                min_instability = instability
                num_operations = 1
            # Check if the instability of the combination is equal to the current minimum
            elif instability == min_instability:
                # Increment the number of operations
                num_operations += 1
    
    # Return the minimum instability and the number of operations
    return min_instability, num_operations

def get_operations(towers, k):
    # Initialize the list of operations
    operations = []
    
    # Loop through all possible combinations of towers
    for i in range(len(towers)):
        for j in range(i+1, len(towers)):
            # Check if the instability of the combination is less than the current minimum
            instability = abs(towers[i] - towers[j])
            if instability == k:
                # Add the operation to the list of operations
                operations.append([i, j])
    
    # Return the list of operations
    return operations

if __name__ == '__main__':
    n, k = map(int, input().split())
    towers = list(map(int, input().split()))
    min_instability, num_operations = get_min_instability(towers, k)
    print(min_instability, num_operations)
    operations = get_operations(towers, k)
    for operation in operations:
        print(*operation)

