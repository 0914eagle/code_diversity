
def arcaea(n, k, partners):
    # Sort the partners in descending order of their Frag values
    partners = sorted(partners, key=lambda x: x[0], reverse=True)

    # Initialize the maximum diversity to be 0
    max_diversity = 0

    # Loop through the partners and try to awaken them
    for i in range(n):
        # Check if the partner can be awakened
        if partners[i][3] != 0:
            # Increment the maximum diversity
            max_diversity += 1

            # Update the partner's Frag and Step values
            partners[i][0] = partners[i][3]
            partners[i][1] = partners[i][4]

            # Break if the maximum diversity is equal to k
            if max_diversity == k:
                break

    # Return the maximum diversity
    return max_diversity

