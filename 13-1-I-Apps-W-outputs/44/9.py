
def solve(s):
    # Initialize a 10x10 matrix to store the results
    matrix = [[0] * 10 for _ in range(10)]

    # Loop through each possible x and y values
    for x in range(10):
        for y in range(10):
            # Skip the case where x and y are the same
            if x == y:
                continue

            # Initialize a variable to store the current value of the counter
            value = 0

            # Loop through each character in the input string
            for i, char in enumerate(s):
                # If the current character is not the same as the current value of the counter, insert a character
                if char != str(value % 10):
                    matrix[x][y] = max(matrix[x][y], i + 1)

                # Add x or y to the current value of the counter, depending on the current character
                value = value * 10 + (x if char == "0" else y)

    return matrix

