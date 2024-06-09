
def add_one(n, cell):
    # Convert the cell string to a list of bits
    cell = [int(bit) for bit in cell]
    # Add 1 to the cell value
    cell = [1 if bit == 0 else 0 for bit in cell]
    # Count the number of bits that change their state
    return sum(cell)

