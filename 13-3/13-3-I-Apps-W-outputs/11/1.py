
import math

def solve(n, m, r, k):
    # Calculate the total number of cells in the pond
    total_cells = n * m
    
    # Calculate the number of possible positions for the scoop-net
    possible_positions = (n - r + 1) * (m - r + 1)
    
    # Calculate the expected value of the number of caught fishes
    expected_value = 0
    for i in range(total_cells):
        # Calculate the number of fishes in each cell
        num_fishes = min(k, total_cells - i)
        # Calculate the probability of catching the fishes in each cell
        probability = num_fishes / total_cells
        # Calculate the expected value of catching the fishes in each cell
        expected_value += probability * num_fishes
    
    # Return the maximum possible expected value of caught fishes
    return expected_value

