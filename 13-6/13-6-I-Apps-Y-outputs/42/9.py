
def solve(R, S, K, picture):
    # Initialize variables
    max_kills = 0
    racket_position = []

    # Iterate through each row of the picture
    for row in range(R):
        # Iterate through each column of the picture
        for col in range(S):
            # If the current pixel is a fly, check if it is within the racket's range
            if picture[row][col] == '*':
                # Check if the fly is within the racket's range
                if col >= K and col <= S - K and row >= K and row <= R - K:
                    # Increment the number of kills
                    max_kills += 1
                    # Add the racket position to the list
                    racket_position.append([row, col])

    # Return the maximum number of kills and the racket position
    return [max_kills, racket_position]

