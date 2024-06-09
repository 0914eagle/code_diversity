
def solve(n, k, chips):
    # Initialize the result string
    result = ""

    # Loop through each iteration
    for i in range(k):
        # Loop through each chip
        for j in range(n):
            # Get the indices of the current chip and its neighbors
            indices = [j-1, j, j+1]
            if j == 0:
                indices[0] = n-1
            if j == n-1:
                indices[2] = 0

            # Count the number of white and black chips among the current chip and its neighbors
            num_white = 0
            num_black = 0
            for index in indices:
                if chips[index] == "W":
                    num_white += 1
                else:
                    num_black += 1

            # Check if the current chip should become white
            if num_white > num_black:
                result += "W"
            else:
                result += "B"

    return result

