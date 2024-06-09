
def solve(n, cell):
    # Convert the cell string to a list of bits
    cell = [int(bit) for bit in cell]
    # Initialize a variable to keep track of the number of changed bits
    changed_bits = 0
    # Iterate through the bits of the cell, starting from the least significant bit
    for i in range(n):
        # If the current bit is 0, set it to 1 and increment the number of changed bits
        if cell[i] == 0:
            cell[i] = 1
            changed_bits += 1
            break
        # If the current bit is 1, set it to 0 and continue to the next bit
        else:
            cell[i] = 0
    # Return the number of changed bits
    return changed_bits

