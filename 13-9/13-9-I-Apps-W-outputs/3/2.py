
def solve(n, bits):
    # Convert the binary string to an integer
    value = int(bits, 2)
    # Add 1 to the value
    value += 1
    # Convert the integer back to a binary string
    bits = bin(value)[2:]
    # Count the number of bits that changed
    return len(bits) - len(set(bits))

