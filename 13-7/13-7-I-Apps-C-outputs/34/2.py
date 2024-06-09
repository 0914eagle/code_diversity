
def max_diversity(n, k, partners):
    # Sort the partners by their Frag values in descending order
    partners = sorted(partners, key=lambda x: x[0], reverse=True)

    # Initialize the maximum diversity and the number of awakened partners
    max_diversity, num_awakened = 0, 0

    # Iterate through the partners
    for partner in partners:
        # Check if the partner can be awakened
        if partner[2] != 0 and num_awakened < k:
            # Increment the number of awakened partners
            num_awakened += 1

            # Update the maximum diversity
            max_diversity = max(max_diversity, partner[1])
        else:
            # Update the maximum diversity
            max_diversity = max(max_diversity, partner[1] + 1)

    # Return the maximum diversity
    return max_diversity

# Main function
if __name__ == "__main__":
    # Read the input
    n, k = map(int, input().split())
    partners = []
    for _ in range(n):
        g, p, g_a, p_a = map(int, input().split())
        partners.append([g, p, g_a, p_a])

    # Call the function to get the maximum diversity
    print(max_diversity(n, k, partners))

