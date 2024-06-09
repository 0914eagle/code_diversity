
def solve(grid):
    # Initialize the shortest ladder length to 0
    shortest_ladder_length = 0

    # Loop through each row of the grid
    for row in grid:
        # Loop through each element in the row
        for element in row:
            # If the element is the special coin, return the shortest ladder length
            if element == "X":
                return shortest_ladder_length
            # If the element is not the special coin, check if the ladder length is less than the current element
            elif element > shortest_ladder_length:
                # If the ladder length is less than the current element, update the shortest ladder length
                shortest_ladder_length = element

    # If the special coin is not found, return 0
    return 0

