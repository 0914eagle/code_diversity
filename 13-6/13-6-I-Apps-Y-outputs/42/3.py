
def solve(R, S, K, picture):
    # Initialize variables
    max_kills = 0
    racket_position = []

    # Iterate through the picture
    for row in range(R):
        for col in range(S):
            # If the current position is a fly, check if it is inside the racket
            if picture[row][col] == "*":
                # Check if the fly is inside the racket
                if row >= racket_position[0] and row <= racket_position[2] and col >= racket_position[1] and col <= racket_position[3]:
                    max_kills += 1

    # Return the maximum number of kills and the racket position
    return max_kills, racket_position

