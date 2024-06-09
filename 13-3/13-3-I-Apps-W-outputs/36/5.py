
def solve(n, m, r, k):
    # Calculate the total number of cells in the pond
    total_cells = n * m
    
    # Calculate the number of possible positions for the scoop-net
    possible_positions = (n - r + 1) * (m - r + 1)
    
    # Calculate the expected number of caught fishes for each position
    expected_caught = 0
    for i in range(possible_positions):
        # Calculate the number of cells inside the scoop-net for this position
        cells_inside = 0
        for j in range(k):
            # Calculate the row and column of the current cell
            row = i // (n - r + 1)
            col = i % (n - r + 1)
            
            # Check if the current cell is inside the scoop-net
            if row >= r and col >= r and row < n - r + 1 and col < m - r + 1:
                cells_inside += 1
        
        # Calculate the expected number of caught fishes for this position
        expected_caught += cells_inside * (cells_inside - 1) / 2
    
    # Calculate the maximum possible expected number of caught fishes
    max_expected_caught = expected_caught / possible_positions
    
    return max_expected_caught

