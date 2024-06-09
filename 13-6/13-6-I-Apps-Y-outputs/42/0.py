
def solve(R, S, K, picture):
    # Initialize variables
    max_kills = 0
    racket_position = []

    # Iterate through each row of the picture
    for i in range(R):
        # Iterate through each column of the picture
        for j in range(S):
            # If the current pixel is a fly, check if it is within the racket's range
            if picture[i][j] == "*":
                # Calculate the distance from the current pixel to the racket's center
                distance = abs(i - (R // 2)) + abs(j - (S // 2))
                # If the distance is less than or equal to the racket's length, it is within the racket's range
                if distance <= K:
                    # Increment the number of kills
                    max_kills += 1
                    # Add the current pixel to the racket position
                    racket_position.append((i, j))

    # Return the maximum number of kills and the racket position
    return max_kills, racket_position

