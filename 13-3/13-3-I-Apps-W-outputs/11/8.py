
import math

def solve(n, m, r, k):
    # Calculate the total number of cells in the pond
    total_cells = n * m
    
    # Calculate the number of possible positions for the scoop-net
    possible_positions = (n - r + 1) * (m - r + 1)
    
    # Calculate the expected value of the number of caught fishes
    expected_value = 0
    for i in range(total_cells):
        # Calculate the number of fishes in the current cell
        num_fishes = 1
        
        # Calculate the number of cells in the current row and column
        row = i // m
        col = i % m
        
        # Calculate the number of cells in the current square
        num_cells = r * r
        
        # Calculate the number of possible positions for the scoop-net in the current square
        possible_positions_square = (row + 1) * (col + 1)
        
        # Calculate the probability of catching a fish in the current cell
        probability = num_cells / possible_positions_square
        
        # Calculate the expected value of the number of caught fishes in the current cell
        expected_value_cell = probability * num_fishes
        
        # Add the expected value of the number of caught fishes in the current cell to the total expected value
        expected_value += expected_value_cell
    
    # Calculate the maximum possible expected value of the number of caught fishes
    max_expected_value = expected_value * k
    
    return max_expected_value

