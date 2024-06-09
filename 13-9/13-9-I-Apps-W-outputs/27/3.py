
def solve(n, votes):
    # Calculate the number of votes Limak needs to have strictly more than any other candidate
    limit = max(votes) + 1

    # Initialize a counter for the number of citizens to bribe
    bribes = 0

    # Iterate through the votes of each candidate
    for i in range(n):
        # If the current candidate has fewer votes than the limit, bribe enough citizens to reach the limit
        while votes[i] < limit:
            bribes += 1
            votes[i] += 1

    return bribes

