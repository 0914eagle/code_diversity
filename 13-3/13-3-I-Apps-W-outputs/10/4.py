
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

def main():
    # Read the input
    n, k = map(int, input().split())
    towers = [list(map(int, input().split())) for _ in range(n)]
    
    # Get the minimum instability and the number of operations
    min_instability, num_operations = get_min_instability(towers, k)
    
    # Print the output
    print(min_instability, num_operations)
    
    # If the minimum instability is 0, there is no need to perform any operations
    if min_instability == 0:
        return
    
    # Loop through the towers
    for i in range(n):
        # If the tower has height 0, skip it
        if towers[i][0] == 0:
            continue
        
        # Get the tower's height
        height = towers[i][0]
        
        # Loop through the other towers
        for j in range(n):
            # If the tower has height 0, skip it
            if towers[j][0] == 0:
                continue
            
            # If the tower has the same height as the current tower, skip it
            if towers[j][0] == height:
                continue
            
            # Print the operation
            print(i+1, j+1)
            
            # Update the tower's height
            towers[j][0] += height
            
            # Break the loop
            break
    
if __name__ == '__main__':
    main()

