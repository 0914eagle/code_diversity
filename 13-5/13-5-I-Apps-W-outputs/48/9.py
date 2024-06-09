
def reconstruct_permutation(n, a, b):
    # Initialize a dictionary to store the counts of each color
    color_counts = {}
    for i in range(n):
        color_counts[a[i]] = color_counts.get(a[i], 0) + 1
        color_counts[b[i]] = color_counts.get(b[i], 0) + 1

    # Initialize a list to store the permutation
    permutation = []

    # Iterate through the colors and add them to the permutation
    for i in range(1, n+1):
        # If the color is in a and not in b, add it to the permutation
        if i in a and i not in b:
            permutation.append(i)
        # If the color is in b and not in a, add it to the permutation
        elif i in b and i not in a:
            permutation.append(i)
        # If the color is in both a and b, add it to the permutation if it is not already there
        elif i in a and i in b and i not in permutation:
            permutation.append(i)

    return permutation

