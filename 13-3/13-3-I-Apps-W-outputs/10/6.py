
def get_min_instability(towers, k):
    # Initialize variables
    min_instability = float('inf')
    min_instability_ops = []
    
    # Iterate over all possible operations
    for i in range(k):
        # Get the current instability
        instability = get_instability(towers)
        
        # If the current instability is less than the minimum, update the minimum and the operations needed
        if instability < min_instability:
            min_instability = instability
            min_instability_ops = []
        
        # If the current instability is equal to the minimum, add the current operations to the list of minimum operations
        if instability == min_instability:
            min_instability_ops.append(i)
    
    # Return the minimum instability and the list of minimum operations
    return min_instability, min_instability_ops

def get_instability(towers):
    # Get the heights of the towers
    heights = [tower[0] for tower in towers]
    
    # Get the maximum and minimum heights
    max_height = max(heights)
    min_height = min(heights)
    
    # Calculate the instability
    instability = max_height - min_height
    
    # Return the instability
    return instability

def main():
    # Read the input
    n, k = map(int, input().split())
    towers = [list(map(int, input().split())) for _ in range(n)]
    
    # Get the minimum instability and the list of minimum operations
    min_instability, min_instability_ops = get_min_instability(towers, k)
    
    # Print the minimum instability and the number of minimum operations
    print(min_instability, len(min_instability_ops))
    
    # Print the minimum operations
    for op in min_instability_ops:
        print(*op)

if __name__ == '__main__':
    main()

