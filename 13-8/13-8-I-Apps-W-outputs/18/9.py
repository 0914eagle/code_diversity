
def solve(n, strength):
    # Initialize a dictionary to store the teammate of each person
    teammates = {}
    # Iterate over the strength of each possible combination of two people
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the strength of the team is the highest among the unpaired people,
            # then the current pair is the best pair
            if strength[i - 1][j - 1] == max(strength[k - 1][l - 1] for k in range(1, n + 1) for l in range(k + 1, n + 1) if k != i and l != j):
                # Add the current pair to the dictionary
                teammates[i] = j
                teammates[j] = i
                break
    # Return the dictionary of teammates
    return teammates

