
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
            energy_required = row[current_position[1]]
            
            # If the energy required is negative, gain energy
            if energy_required < 0:
                current_energy += energy_required
            # Otherwise, lose energy
            else:
                current_energy -= energy_required
            
            # If the current energy is less than or equal to 0, break the loop
            if current_energy <= 0:
                break
            
            # Move up or down depending on the energy required
            if energy_required > 0:
                current_position = (current_position[0] + 1, current_position[1])
            else:
                current_position = (current_position[0] - 1, current_position[1])
        
        # If the current energy is greater than or equal to 0, update the minimum energy required
        if current_energy >= 0:
            min_energy = min(min_energy, current_energy)
    
    return min_energy

def main():
    # Read the input
    R, C = map(int, input().split())
    cliff = []
    for _ in range(R):
        cliff.append(list(map(int, input().split())))
    start_points = list(input().split())
    
    # Get the minimum energy required to complete the climb
    min_energy = get_min_energy(cliff, start_points)
    
    # Print the minimum energy required
    print(min_energy)

if __name__ == '__main__':
    main()

