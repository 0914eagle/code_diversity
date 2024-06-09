
def solve(n, k, partners):
    # Sort the partners by their Frag and Step values
    partners = sorted(partners, key=lambda x: (x[0], x[1]))

    # Initialize the maximum diversity to be 0
    max_diversity = 0

    # Iterate through the partners and choose the k most favorable partners to awaken
    for i in range(k):
        # If the current partner cannot be awakened, skip it
        if partners[i][2] == 0 or partners[i][3] == 0:
            continue

        # Increment the maximum diversity by 1
        max_diversity += 1

        # Update the Frag and Step values of the current partner
        partners[i][0] = partners[i][2]
        partners[i][1] = partners[i][3]

    # Return the maximum diversity
    return max_diversity

