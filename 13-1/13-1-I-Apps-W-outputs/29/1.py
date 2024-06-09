
def count_dress_patterns(n, m, fabric):
    # Initialize a dictionary to store the number of dress patterns for each size
    dress_patterns = {}

    # Loop through each row of the fabric
    for i in range(n):
        # Loop through each column of the fabric
        for j in range(m):
            # Get the color of the current scrap
            color = fabric[i][j]

            # Check if the current scrap is part of a dress pattern
            if color in dress_patterns:
                # If it is, increment the number of dress patterns for the current size
                dress_patterns[color] += 1
            else:
                # If it's not, create a new entry for the current size
                dress_patterns[color] = 1

    # Return the total number of dress patterns
    return sum(dress_patterns.values())

