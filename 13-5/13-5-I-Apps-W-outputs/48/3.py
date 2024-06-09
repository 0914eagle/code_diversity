
def reconstruct_permutation(n, a, b):
    # Initialize a dictionary to store the counts of each color
    color_count = {}
    for i in range(n):
        color_count[a[i]] = color_count.get(a[i], 0) + 1
        color_count[b[i]] = color_count.get(b[i], 0) + 1

    # Initialize a list to store the permutation
    permutation = []

    # Iterate through the colors and add them to the permutation
    for i in range(1, n+1):
        if color_count[i] == 1:
            permutation.append(i)

    return permutation

