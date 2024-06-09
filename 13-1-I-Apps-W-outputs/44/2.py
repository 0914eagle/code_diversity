
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
                # If the current character is not equal to the current value of the counter, break the loop
                if char != str(value % 10):
                    break

                # Add x or y to the current value of the counter, depending on the current character
                value += x if char == "0" else y

            # If we reached the end of the input string, the current value of the counter is a valid output
            if i == len(s) - 1:
                # Update the matrix with the minimum number of digits needed to make the output valid
                matrix[x][y] = len(s) - i

    return matrix

