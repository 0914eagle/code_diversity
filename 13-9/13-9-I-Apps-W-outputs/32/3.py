
def solve(n, k, chips):
    # Initialize the results array
    results = [""] * n

    # Loop through each iteration
    for i in range(k):
        # Loop through each chip
        for j in range(n):
            # Get the indices of the three neighbors
            indices = [j - 1, j, j + 1]
            indices[0] = indices[0] % n
            indices[2] = indices[2] % n

            # Count the number of white and black chips among the three neighbors
            white_count = 0
            black_count = 0
            for index in indices:
                if chips[index] == "W":
                    white_count += 1
                else:
                    black_count += 1

            # Update the result for the current chip
            if white_count > black_count:
                results[j] = "W"
            else:
                results[j] = "B"

    # Return the final results
    return "".join(results)

