
def solve(n, cell_state):
    # Convert the cell state string to a list of integers
    cell_state = [int(x) for x in cell_state]
    # Initialize a variable to keep track of the number of changed bits
    changed_bits = 0
    # Iterate through the bits of the cell, starting from the least significant bit
    for i in range(n):
        # If the current bit is 0, set it to 1 and increment the number of changed bits
        if cell_state[i] == 0:
            cell_state[i] = 1
            changed_bits += 1
            break
        # If the current bit is 1, set it to 0 and continue to the next bit
        else:
            cell_state[i] = 0
    # Return the number of changed bits
    return changed_bits

