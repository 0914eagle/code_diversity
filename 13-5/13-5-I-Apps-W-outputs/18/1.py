
def solve(grid):
    # Initialize the number of even and odd cells
    num_even = 0
    num_odd = 0
    
    # Iterate through the grid and count the number of even and odd cells
    for row in grid:
        for cell in row:
            if cell % 2 == 0:
                num_even += 1
            else:
                num_odd += 1
    
    # If the number of even cells is greater than the number of odd cells, return the sequence of operations to maximize the number of even cells
    if num_even > num_odd:
        return "0"
    
    # If the number of odd cells is greater than the number of even cells, return the sequence of operations to maximize the number of odd cells
    elif num_odd > num_even:
        return "1"
    
    # If the number of even cells is equal to the number of odd cells, return the sequence of operations to maximize the number of even cells
    else:
        return "2"

