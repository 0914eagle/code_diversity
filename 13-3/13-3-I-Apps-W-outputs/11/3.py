
import math

def solve(n, m, r, k):
    # Calculate the total number of cells in the pond
    total_cells = n * m
    
    # Calculate the number of possible positions for the scoop-net
    possible_positions = (n - r + 1) * (m - r + 1)
    
    # Calculate the expected number of caught fishes for each position
    expected_caught_fishes = []
    for i in range(possible_positions):
        # Calculate the number of fishes in each cell for this position
        cell_fishes = [0] * total_cells
        for j in range(k):
            # Calculate the index of the cell where the fish will be placed
            cell_index = (i * k + j) % total_cells
            cell_fishes[cell_index] += 1
        
        # Calculate the expected number of caught fishes for this position
        expected_caught_fishes.append(sum(cell_fishes) / k)
    
    # Return the maximum expected number of caught fishes
    return max(expected_caught_fishes)

