
def solve(n, k, partners):
    # Sort the partners in descending order of their Frag values
    partners = sorted(partners, key=lambda x: x[0], reverse=True)

    # Initialize the maximum diversity to be 0
    max_diversity = 0

    # Iterate over the first k partners
    for i in range(k):
        # Get the current partner
        partner = partners[i]

        # If the partner cannot be awakened, skip it
        if partner[2] == 0:
            continue

        # Get the partner's new Frag and Step values after awakening
        new_frag, new_step = partner[2], partner[3]

        # Update the maximum diversity
        max_diversity = max(max_diversity, new_frag - partner[0], new_step - partner[1])

    # Return the maximum diversity
    return max_diversity

