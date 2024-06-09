
def solve(n, m, r, k):
    # Calculate the total number of cells in the pond
    total_cells = n * m
    
    # Calculate the number of possible positions for the scoop-net
    possible_positions = (n - r + 1) * (m - r + 1)
    
    # Calculate the expected value of the number of caught fishes
    expected_value = 0
    for i in range(total_cells):
        # Calculate the number of fishes in the current cell
        num_fishes = min(k, total_cells - i)
        
        # Calculate the probability of the current cell being inside the scoop-net
        probability = 1 / possible_positions
        
        # Add the product of the number of fishes and probability to the expected value
        expected_value += num_fishes * probability
    
    return expected_value

