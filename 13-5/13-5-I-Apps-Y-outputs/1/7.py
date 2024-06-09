
def solve(n, k):
    # Initialize a list to store the colors of the costumes
    costumes = [[0, 0] for _ in range(n)]

    # Iterate over the pairs
    for i in range(n):
        # If this is not the first pair, make sure the colors are different from the previous pair
        if i > 0:
            while costumes[i][0] == costumes[i-1][0] or costumes[i][1] == costumes[i-1][1]:
                costumes[i][0] = random.randint(1, k)
                costumes[i][1] = random.randint(1, k)

        # Make sure the colors are different from each other
        while costumes[i][0] == costumes[i][1]:
            costumes[i][1] = random.randint(1, k)

    # Check if there are any two consecutive pairs with the same colors
    for i in range(n-1):
        if costumes[i][0] == costumes[i+1][0] and costumes[i][1] == costumes[i+1][1]:
            return "NO"

    # If we reach here, it means we have found a valid color choosing
    return "YES\n" + "\n".join([str(costumes[i][0]) + " " + str(costumes[i][1]) for i in range(n)])

