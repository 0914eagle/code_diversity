
def solve(n, k, chips):
    # Initialize the result string
    result = ""

    # Loop through each iteration
    for i in range(k):
        # Loop through each chip
        for j in range(n):
            # Find the neighbors of the current chip
            neighbors = []
            if j == 0:
                neighbors = [n - 1, j + 1]
            elif j == n - 1:
                neighbors = [j - 1, 0]
            else:
                neighbors = [j - 1, j + 1]

            # Count the number of white and black neighbors
            white_neighbors = 0
            black_neighbors = 0
            for neighbor in neighbors:
                if chips[neighbor] == "W":
                    white_neighbors += 1
                else:
                    black_neighbors += 1

            # Check if the current chip should be white or black
            if white_neighbors > black_neighbors:
                result += "W"
            else:
                result += "B"

    return result

