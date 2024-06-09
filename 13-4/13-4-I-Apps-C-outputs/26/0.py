
def get_min_energy(cliff, start_points):
    # Initialize the minimum energy required to complete the climb
    min_energy = float('inf')
    
    # Loop through all possible start points
    for start_point in start_points:
        # Initialize the current energy required to complete the climb
        current_energy = 0
        
        # Loop through all rows of the cliff
        for row in cliff:
            # Loop through all columns of the current row
            for column in row:
                # Add the energy required to enter the current square to the current energy
                current_energy += column
                
                # If the current energy is negative, break out of the loop
                if current_energy < 0:
                    break
        
        # If the current energy is less than the minimum energy required to complete the climb, update the minimum energy
        if current_energy < min_energy:
            min_energy = current_energy
    
    # Return the minimum energy required to complete the climb
    return min_energy

def main():
    # Read the input
    R, C = map(int, input().split())
    cliff = [list(map(int, input().split())) for _ in range(R)]
    start_points = list(input())
    
    # Get the minimum energy required to complete the climb
    min_energy = get_min_energy(cliff, start_points)
    
    # Print the minimum energy required to complete the climb
    print(min_energy)

if __name__ == '__main__':
    main()

