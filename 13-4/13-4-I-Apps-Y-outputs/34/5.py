
def get_signatures(K, desk_numbers):
    # Initialize a list to store the signatures
    signatures = []

    # Iterate through the desk numbers
    for desk_number in desk_numbers:
        # If the desk number is not in the list of signatures, add it
        if desk_number not in signatures:
            signatures.append(desk_number)

    # Return the number of signatures collected
    return len(signatures)

