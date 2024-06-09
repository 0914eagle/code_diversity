
def get_min_instability(towers, k):
    # Initialize the minimum instability and the number of operations
    min_instability = float('inf')
    num_operations = 0
    
    # Loop through all possible sequences of operations
    for i in range(1, k+1):
        # Get the current instability
        instability = get_instability(towers)
        
        # If the current instability is less than the minimum instability, update the minimum instability and the number of operations
        if instability < min_instability:
            min_instability = instability
            num_operations = i
        
        # If the current instability is equal to the minimum instability, update the number of operations
        elif instability == min_instability:
            num_operations = min(num_operations, i)
    
    # Return the minimum instability and the number of operations
    return min_instability, num_operations

def get_instability(towers):
    # Get the heights of the towers
    heights = [tower[0] for tower in towers]
    
    # Get the maximum and minimum heights
    max_height = max(heights)
    min_height = min(heights)
    
    # Return the instability
    return max_height - min_height

def get_operations(towers, num_operations):
    # Initialize the operations list
    operations = []
    
    # Loop through the number of operations
    for i in range(num_operations):
        # Get the current tower
        current_tower = towers[i % len(towers)]
        
        # Get the top cube from the current tower
        top_cube = current_tower[0]
        
        # Remove the top cube from the current tower
        current_tower.pop(0)
        
        # Add the top cube to the next tower
        next_tower = towers[(i+1) % len(towers)]
        next_tower.append(top_cube)
        
        # Add the operation to the list of operations
        operations.append([i+1, i+2])
    
    # Return the list of operations
    return operations

if __name__ == '__main__':
    # Read the input
    n, k = map(int, input().split())
    towers = [list(map(int, input().split())) for _ in range(n)]
    
    # Get the minimum instability and the number of operations
    min_instability, num_operations = get_min_instability(towers, k)
    
    # Get the list of operations
    operations = get_operations(towers, num_operations)
    
    # Print the minimum instability and the number of operations
    print(min_instability, num_operations)
    
    # Print the list of operations
    for operation in operations:
        print(' '.join(map(str, operation)))

