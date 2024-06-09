
def solve(n, k, partners):
    # Sort the partners by their Frag and Step values
    partners = sorted(partners, key=lambda x: (x[0], x[1]), reverse=True)

    # Initialize the maximum diversity to be 0
    max_diversity = 0

    # Initialize the number of awakened partners to be 0
    num_awakened = 0

    # Iterate through the partners
    for partner in partners:
        # Check if the partner can be awakened
        if partner[2] != 0 and partner[3] != 0:
            # Increment the number of awakened partners
            num_awakened += 1

            # Check if the number of awakened partners is less than or equal to k
            if num_awakened <= k:
                # Increment the maximum diversity
                max_diversity += 1

    # Return the maximum diversity
    return max_diversity

