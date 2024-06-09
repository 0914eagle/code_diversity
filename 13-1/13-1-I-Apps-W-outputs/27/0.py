
def reconstruct_permutation(n, a, b):
    # Initialize a dictionary to store the counts of each color
    color_counts = {}
    for i in range(n):
        color_counts[a[i]] = color_counts.get(a[i], 0) + 1
        color_counts[b[i]] = color_counts.get(b[i], 0) + 1

    # Initialize a list to store the permutation
    permutation = []

    # Iterate through the dictionary and add the colors to the permutation
    for color, count in color_counts.items():
        for i in range(count):
            permutation.append(color)

    return permutation

