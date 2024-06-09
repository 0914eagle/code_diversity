
def solve(R, S, K, picture):
    # Initialize variables
    max_kills = 0
    racket_position = []

    # Iterate through each row of the picture
    for i in range(R):
        # Iterate through each column of the current row
        for j in range(S):
            # If the current pixel is a fly, check if it is within the racket's reach
            if picture[i][j] == "*":
                # Check if the fly is within the racket's reach
                if i - K + 1 >= 0 and j - K + 1 >= 0 and i + K <= R - 1 and j + K <= S - 1:
                    # Increment the number of kills
                    max_kills += 1
                    # Add the fly's position to the racket's position
                    racket_position.append((i, j))

    # Return the maximum number of kills and the racket's position
    return max_kills, racket_position

