
def solve(n, cell):
    # Convert the cell state to an integer
    cell_int = int(cell, 2)

    # Add 1 to the cell value
    cell_int += 1

    # Convert the new cell value back to a binary string
    cell_bin = bin(cell_int)[2:]

    # Count the number of bits that changed
    changed_bits = 0
    for i in range(n):
        if cell[i] != cell_bin[i]:
            changed_bits += 1

    return changed_bits

