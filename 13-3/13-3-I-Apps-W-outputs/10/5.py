
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
        
        # Perform the next operation
        perform_operation(towers)
    
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

def perform_operation(towers):
    # Choose a random tower
    tower_index = random.randint(0, len(towers) - 1)
    
    # Get the current height of the tower
    tower_height = towers[tower_index][0]
    
    # If the tower is not empty, remove the top cube
    if tower_height > 0:
        towers[tower_index][0] -= 1
    
    # Choose a random tower to put the cube on
    target_tower_index = random.randint(0, len(towers) - 1)
    
    # Put the cube on the target tower
    towers[target_tower_index][0] += 1

if __name__ == '__main__':
    n, k = map(int, input().split())
    towers = []
    for _ in range(n):
        towers.append([int(input())])
    min_instability, num_operations = get_min_instability(towers, k)
    print(min_instability, num_operations)
    for i in range(num_operations):
        print(random.randint(1, n), random.randint(1, n))

