
def solve(R, S, K, picture):
    # Initialize variables
    max_kills = 0
    racket_position = []

    # Iterate through each row of the picture
    for i in range(R):
        # Iterate through each column of the picture
        for j in range(S):
            # If the current pixel is a fly, check if it can be killed with the racket
            if picture[i][j] == "*":
                # Check if the fly is within the racket's range
                if i >= K and j >= K and i < R - K and j < S - K:
                    # Increment the number of kills
                    max_kills += 1
                    # Add the fly's position to the racket position
                    racket_position.append((i, j))

    # Return the maximum number of kills and the racket position
    return max_kills, racket_position

