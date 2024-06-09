
def get_min_energy(cliff, start_points):
    # Initialize the minimum energy required to complete the climb
    min_energy = float('inf')
    
    # Loop through all possible start points
    for start_point in start_points:
        # Initialize the current energy and position
        current_energy = 0
        current_position = start_point
        
        # Loop through all rows of the cliff
        for row in cliff:
            # Get the energy required to enter the current position
            energy_required = row[current_position]
            
            # Check if the current energy is less than the minimum energy required to complete the climb
            if current_energy < min_energy:
                # Update the minimum energy required to complete the climb
                min_energy = current_energy
                
            # Check if the current energy is negative
            if current_energy < 0:
                # Break out of the loop and try a different start point
                break
                
            # Update the current energy and position
            current_energy -= energy_required
            current_position = (current_position + 1) % len(row)
    
    # Return the minimum energy required to complete the climb
    return min_energy

def main():
    # Read the input from stdin
    R, C = map(int, input().split())
    cliff = [list(map(int, input().split())) for _ in range(R)]
    start_points = list(map(int, input().split()))
    
    # Call the get_min_energy function and print the result
    print(get_min_energy(cliff, start_points))

if __name__ == '__main__':
    main()

