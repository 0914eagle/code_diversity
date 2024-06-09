
def solve(n, m, r, k):
    # Calculate the total number of cells in the pond
    total_cells = n * m
    
    # Calculate the number of cells that are inside the scoop-net
    inside_cells = (r * 2 + 1) ** 2
    
    # Calculate the number of cells that are outside the scoop-net
    outside_cells = total_cells - inside_cells
    
    # Calculate the expected number of caught fishes
    expected_caught = k * inside_cells / total_cells
    
    return expected_caught

