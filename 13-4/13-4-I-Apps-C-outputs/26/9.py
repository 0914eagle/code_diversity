
def get_energy_required(cliff, start_point):
    # Initialize the energy required to be 0
    energy_required = 0
    
    # Loop through the cliff
    for row in cliff:
        for cell in row:
            # If the cell is not empty, add the energy required to the total energy required
            if cell != "E":
                energy_required += int(cell)
    
    # Return the total energy required
    return energy_required

def get_min_energy_required(cliff, start_points):
    # Initialize the minimum energy required to be infinity
    min_energy_required = float("inf")
    
    # Loop through the start points
    for start_point in start_points:
        # Get the energy required to reach the start point
        energy_required = get_energy_required(cliff, start_point)
        
        # If the energy required is less than the minimum energy required, update the minimum energy required
        if energy_required < min_energy_required:
            min_energy_required = energy_required
    
    # Return the minimum energy required
    return min_energy_required

def main():
    # Read the input
    R, C = map(int, input().split())
    cliff = [input().split() for _ in range(R)]
    start_points = input().split()
    
    # Get the minimum energy required to complete the climb
    min_energy_required = get_min_energy_required(cliff, start_points)
    
    # Print the minimum energy required
    print(min_energy_required)

if __name__ == '__main__':
    main()

