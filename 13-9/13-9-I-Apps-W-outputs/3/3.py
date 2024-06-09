
def get_changed_bits(n, bits):
    # Convert the binary string to an integer
    value = int(bits, 2)
    # Add 1 to the integer
    value += 1
    # Convert the integer back to a binary string
    bits = bin(value)[2:]
    # Return the number of bits that changed
    return len(bits)

