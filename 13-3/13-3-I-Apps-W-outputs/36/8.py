
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
        # Calculate the probability of catching fishes in each cell
        prob = num_fishes / total_cells
        # Add the product of probability and number of fishes to the expected value
        expected_value += prob * num_fishes
    
    return expected_value

