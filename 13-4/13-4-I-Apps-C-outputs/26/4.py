
def get_energy_required(cliff):
    # Initialize a dictionary to store the minimum energy required to reach each square
    energy_required = {}
    
    # Initialize the starting position with 0 energy
    energy_required[0, 0] = 0
    
    # Loop through each row and column of the cliff
    for r in range(len(cliff)):
        for c in range(len(cliff[0])):
            # If the current square is not the starting position, check if the minimum energy required to reach it has already been calculated
            if (r, c) != (0, 0) and (r, c) not in energy_required:
                # If the current square is not the starting position and the minimum energy required to reach it has not been calculated, calculate it
                energy_required[r, c] = min(energy_required[r-1, c], energy_required[r, c-1], energy_required[r+1, c], energy_required[r, c+1]) + cliff[r][c]
    
    # Return the minimum energy required to reach the bottom-right square of the cliff
    return energy_required[len(cliff)-1, len(cliff[0])-1]

def get_starting_position(cliff):
    # Initialize a list to store the possible starting positions
    starting_positions = []
    
    # Loop through each row and column of the cliff
    for r in range(len(cliff)):
        for c in range(len(cliff[0])):
            # If the current square is a starting position, add it to the list of possible starting positions
            if cliff[r][c] == 'S':
                starting_positions.append((r, c))
    
    # Return the list of possible starting positions
    return starting_positions

def get_minimum_energy_required(cliff):
    # Get the minimum energy required to reach the bottom-right square of the cliff for each possible starting position
    minimum_energy_required = [get_energy_required(cliff) for cliff in get_starting_position(cliff)]
    
    # Return the minimum of the minimum energy required for each possible starting position
    return min(minimum_energy_required)

if __name__ == '__main__':
    # Read the input
    R, C = map(int, input().split())
    cliff = [list(map(int, input().split())) for _ in range(R)]
    S = list(map(int, input().split()))
    
    # Get the minimum energy required to complete the climb
    minimum_energy_required = get_minimum_energy_required(cliff)
    
    # Print the minimum energy required
    print(minimum_energy_required)

