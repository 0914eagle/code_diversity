
def reconstruct_permutation(n, a, b):
    # Initialize a dictionary to store the counts of each color
    color_count = {}
    for i in range(n):
        color_count[a[i]] = color_count.get(a[i], 0) + 1
        color_count[b[i]] = color_count.get(b[i], 0) + 1

    # Initialize a list to store the permutation
    permutation = []

    # Iterate through the dictionary and add the colors to the permutation
    for color, count in color_count.items():
        for i in range(count):
            permutation.append(color)

    return permutation

