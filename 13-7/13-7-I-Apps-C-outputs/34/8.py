
def get_max_diversity(partners, k):
    # Sort the partners in descending order of their Frag values
    partners.sort(key=lambda x: x[0], reverse=True)

    # Initialize the maximum diversity and the number of awakened partners
    max_diversity, num_awakened = 0, 0

    # Iterate through the sorted partners
    for partner in partners:
        # Check if the partner can be awakened
        if partner[2] != 0 and num_awakened < k:
            # Increment the number of awakened partners
            num_awakened += 1

            # Update the maximum diversity
            max_diversity = max(max_diversity, partner[3])
        else:
            # Update the maximum diversity
            max_diversity = max(max_diversity, partner[1])

    # Return the maximum diversity
    return max_diversity

