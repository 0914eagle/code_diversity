
def get_min_height(n, m):
    # Initialize a list to store the heights of the towers
    heights = []

    # Add the heights of the towers made with two-block pieces
    for i in range(1, n + 1):
        heights.append(i * 2)

    # Add the heights of the towers made with three-block pieces
    for i in range(1, m + 1):
        heights.append(i * 3)

    # Sort the list in ascending order
    heights.sort()

    # Return the last element of the sorted list, which is the maximum height
    return heights[-1]

