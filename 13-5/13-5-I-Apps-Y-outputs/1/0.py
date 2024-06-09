
def solve_ball_problem(n, k):
    # Initialize a list to store the colors of the costumes
    costumes = [[0, 0] for _ in range(n)]

    # Iterate through the pairs
    for i in range(n):
        # If this is not the first pair, make sure the colors are different
        if i > 0:
            # Check if the colors of the previous pair are the same
            if costumes[i - 1][0] == costumes[i - 1][1]:
                return "NO"

        # Choose a color for the man's costume
        costumes[i][0] = (i % k) + 1

        # Choose a color for the woman's costume that is different from the man's color
        costumes[i][1] = (costumes[i][0] % k) + 1

    # Print the colors of the costumes
    print("YES")
    for pair in costumes:
        print(pair[0], pair[1])

    return "YES"

