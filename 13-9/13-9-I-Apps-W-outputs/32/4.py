
def solve(n, k, chips):
    # Initialize the result string
    result = ""

    # Iterate over the given number of iterations
    for i in range(k):
        # Iterate over the chips
        for j in range(n):
            # Get the indices of the three neighbors
            indices = [j - 1, j, j + 1]
            if j == 0:
                indices[0] = n - 1
            if j == n - 1:
                indices[2] = 0

            # Count the number of white and black chips among the neighbors
            num_white = 0
            num_black = 0
            for index in indices:
                if chips[index] == "W":
                    num_white += 1
                else:
                    num_black += 1

            # Set the color of the current chip according to the rules
            if num_white > num_black:
                chips[j] = "W"
            else:
                chips[j] = "B"

        # Update the result string
        result += "".join(chips)

    return result

