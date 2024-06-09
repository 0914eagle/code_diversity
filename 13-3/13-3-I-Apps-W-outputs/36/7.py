
def solve(n, m, r, k):
    # Calculate the total number of cells in the pond
    total_cells = n * m
    
    # Calculate the number of possible positions for the scoop-net
    possible_positions = (n - r + 1) * (m - r + 1)
    
    # Calculate the expected number of caught fishes for each position
    expected_caught = 0
    for i in range(possible_positions):
        # Calculate the number of fishes in the current position
        num_fishes = 0
        for j in range(k):
            # Calculate the row and column of the current fish
            row = (i // (m - r + 1)) + 1
            col = (i % (m - r + 1)) + 1
            
            # Check if the current fish is in the current position
            if row >= r and col >= r and row <= n - r + 1 and col <= m - r + 1:
                num_fishes += 1
        
        # Calculate the expected number of caught fishes for the current position
        expected_caught += num_fishes / possible_positions
    
    return expected_caught

