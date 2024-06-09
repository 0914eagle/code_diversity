
def solve(n, k, chips):
    # Initialize the result string
    result = ""

    # Iterate over the given number of iterations
    for i in range(k):
        # Iterate over the chips
        for j in range(n):
            # Find the indices of the three neighbors
            indices = [j-1, j, j+1]
            indices[0] = indices[0] % n
            indices[2] = indices[2] % n

            # Count the number of white and black chips among the neighbors
            white_neighbors = 0
            black_neighbors = 0
            for idx in indices:
                if chips[idx] == "W":
                    white_neighbors += 1
                else:
                    black_neighbors += 1

            # Update the current chip based on the number of white and black neighbors
            if white_neighbors > black_neighbors:
                chips[j] = "W"
            else:
                chips[j] = "B"

        # Update the result string
        result += "".join(chips)

    return result

