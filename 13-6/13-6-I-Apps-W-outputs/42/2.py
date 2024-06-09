
def get_unfairness(n):
    # Convert the number to binary
    binary = bin(n)[2:]
    # Initialize the unfairness variable
    unfairness = 0
    # Iterate over the binary string
    for i in range(len(binary) - 1):
        # Calculate the difference between the current and next number
        diff = int(binary[i + 1]) - int(binary[i])
        # Add the difference to the unfairness
        unfairness += diff
    # Return the unfairness
    return unfairness

