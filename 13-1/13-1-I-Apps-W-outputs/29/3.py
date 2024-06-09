
def count_dress_patterns(n, m, fabric):
    # Initialize a dictionary to store the number of dress patterns for each size
    dress_patterns = {1: 0, 2: 0, 3: 0, 4: 0}

    # Loop through each row of the fabric
    for i in range(n):
        # Loop through each column of the fabric
        for j in range(m):
            # If the current square is part of a dress pattern, increment the corresponding size
            if fabric[i][j] == 'a':
                dress_patterns[1] += 1
            elif fabric[i][j] == 'b':
                dress_patterns[2] += 1
            elif fabric[i][j] == 'c':
                dress_patterns[3] += 1
            elif fabric[i][j] == 'd':
                dress_patterns[4] += 1

    # Return the sum of the number of dress patterns for each size
    return sum(dress_patterns.values())

