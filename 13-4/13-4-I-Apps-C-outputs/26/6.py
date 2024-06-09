
def get_energy_required(cliff):
    
    # Initialize the energy required to be the maximum possible value
    energy_required = float('inf')
    
    # Iterate over all possible starting points
    for start_point in cliff[0]:
        # Initialize the current energy to be 0
        current_energy = 0
        
        # Iterate over all rows of the cliff
        for row in cliff[1:]:
            # Find the minimum energy required to reach the next square
            min_energy = float('inf')
            for col in row:
                if col != 'S':
                    min_energy = min(min_energy, abs(int(col)))
            
            # Add the minimum energy required to the current energy
            current_energy += min_energy
            
            # If the current energy is negative, return 0 as the minimum energy required
            if current_energy < 0:
                return 0
        
        # Update the energy required if the current energy is less than the previous minimum
        energy_required = min(energy_required, current_energy)
    
    # Return the minimum energy required
    return energy_required

def main():
    # Read the input
    R, C = map(int, input().split())
    cliff = []
    for _ in range(R):
        cliff.append(list(input()))
    
    # Get the minimum energy required to complete the climb
    energy_required = get_energy_required(cliff)
    
    # Print the minimum energy required
    print(energy_required)

if __name__ == '__main__':
    main()

