
def get_signatures(K, desks):
    # Initialize a list to store the signatures
    signatures = []

    # Iterate through the desks in increasing order
    for desk in sorted(desks):
        # If the desk is not in the signatures list, add it
        if desk not in signatures:
            signatures.append(desk)

    # Return the number of signatures needed
    return len(signatures)

