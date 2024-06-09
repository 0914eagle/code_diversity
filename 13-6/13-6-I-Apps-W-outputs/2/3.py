
def solve(n, s):
    # Initialize the number of sets to 0
    sets = 0
    # Iterate over the rounds
    for i in range(n):
        # If the current round is won by Alice
        if s[i] == "0":
            # Increment the number of sets
            sets += 1
        # If the current round is won by Bob
        elif s[i] == "1":
            # Reset the number of sets to 0
            sets = 0
    # Return the number of sets
    return sets

