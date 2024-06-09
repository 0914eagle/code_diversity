
def arcaea(n, k, partners):
    # Sort the partners by their frag and step values
    sorted_partners = sorted(partners, key=lambda x: (x[0], x[1]))

    # Initialize the maximum diversity as 0
    max_diversity = 0

    # Iterate through the partners and choose the k most favorable partners to awaken
    for i in range(k):
        # Add the current partner to the list of awakened partners
        awakened_partners.append(sorted_partners[i])

        # Update the maximum diversity
        max_diversity = max(max_diversity, i + 1)

    # Return the maximum diversity
    return max_diversity

