
def get_signatures(K, desk_numbers):
    # Initialize a list to store the signatures
    signatures = []

    # Iterate through the desk numbers
    for desk_number in desk_numbers:
        # If the desk number is not in the signatures list, add it
        if desk_number not in signatures:
            signatures.append(desk_number)

    # Sort the signatures list in ascending order
    signatures.sort()

    # Initialize a counter for the number of passes
    passes = 0

    # Iterate through the signatures list
    for i in range(len(signatures)):
        # If the current signature is not in the correct position, increment the passes counter
        if signatures[i] != i + 1:
            passes += 1

    # Return the number of passes
    return passes

