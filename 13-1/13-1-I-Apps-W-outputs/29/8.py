
def count_dress_patterns(n, m, fabric):
    # Initialize a dictionary to store the number of dress patterns for each size
    dress_patterns = {1: 0, 2: 0, 3: 0, 4: 0}

    # Loop through each row of the fabric
    for i in range(n):
        # Loop through each column of the fabric
        for j in range(m):
            # Check if the current square is part of a dress pattern
            if is_dress_pattern(i, j, fabric):
                # Increment the number of dress patterns for the current size
                dress_patterns[len(get_dress_pattern(i, j, fabric))] += 1

    # Return the total number of dress patterns
    return sum(dress_patterns.values())

def is_dress_pattern(i, j, fabric):
    # Check if the current square is part of a dress pattern
    if fabric[i][j] == 'a':
        return True
    else:
        return False

def get_dress_pattern(i, j, fabric):
    # Initialize a list to store the dress pattern
    pattern = []

    # Loop through the rows and columns of the fabric
    for row in range(i, n):
        for col in range(j, m):
            # Check if the current square is part of the dress pattern
            if fabric[row][col] == 'a':
                # Add the current square to the dress pattern
                pattern.append((row, col))

    # Return the dress pattern
    return pattern

n, m = map(int, input().split())
fabric = [input() for _ in range(n)]
print(count_dress_patterns(n, m, fabric))

