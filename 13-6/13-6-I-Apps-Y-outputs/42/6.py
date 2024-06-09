
def solve(R, S, K, picture):
    # Initialize variables
    max_kills = 0
    racket_position = []

    # Iterate over each row of the picture
    for i in range(R):
        # Iterate over each column of the picture
        for j in range(S):
            # If the current pixel is a fly, check if it is within the racket's range
            if picture[i][j] == "*":
                # Calculate the distance between the current pixel and the racket's center
                distance = abs(i - (R // 2)) + abs(j - (S // 2))
                # If the distance is less than or equal to the racket's length, increment the kill count
                if distance <= K:
                    max_kills += 1
                    # Add the current pixel to the racket's position
                    racket_position.append((i, j))

    # Return the maximum kill count and the racket's position
    return max_kills, racket_position

