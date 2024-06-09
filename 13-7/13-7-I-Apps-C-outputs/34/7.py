
def get_max_diversity(n, k, partners):
    # Sort the partners in descending order of their Frag values
    partners.sort(key=lambda x: x[0], reverse=True)

    # Initialize the maximum diversity to be 0
    max_diversity = 0

    # Initialize the current diversity to be 0
    current_diversity = 0

    # Initialize the number of awakened partners to be 0
    num_awakened = 0

    # Iterate through the partners
    for partner in partners:
        # If the partner cannot be awakened, skip it
        if partner[2] == 0:
            continue

        # If the partner can be awakened and the number of awakened partners is less than k, awaken the partner
        if partner[2] != 0 and num_awakened < k:
            # Increment the number of awakened partners
            num_awakened += 1

            # Add the partner's new Frag and Step values to the current diversity
            current_diversity += partner[2] + partner[3]

        # If the current diversity is greater than the maximum diversity, update the maximum diversity
        if current_diversity > max_diversity:
            max_diversity = current_diversity

    # Return the maximum diversity
    return max_diversity


n, k = map(int, input().split())
partners = []
for _ in range(n):
    g, p, g_a, p_a = map(int, input().split())
    partners.append([g, p, g_a, p_a])

print(get_max_diversity(n, k, partners))

