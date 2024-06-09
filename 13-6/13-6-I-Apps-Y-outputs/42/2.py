
def solve(R, S, K, picture):
    # Initialize variables
    max_kills = 0
    racket_position = []

    # Iterate through the picture
    for i in range(R):
        for j in range(S):
            # Check if the current pixel is a fly
            if picture[i][j] == "*":
                # Calculate the number of flies that can be killed with the current racket position
                kills = 0
                for k in range(i, i+K):
                    for l in range(j, j+K):
                        if k < R and l < S and picture[k][l] == "*":
                            kills += 1

                # Update the maximum number of kills and the racket position if necessary
                if kills > max_kills:
                    max_kills = kills
                    racket_position = [i, j]

    # Return the maximum number of kills and the racket position
    return [max_kills, racket_position]

