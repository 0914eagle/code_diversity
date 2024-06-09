
def solve(n, a):
    # Find the candidate with the most votes
    max_votes = max(a)
    max_index = a.index(max_votes)

    # Calculate the number of votes Limak needs to win
    votes_needed = max_votes - a[0] + 1

    # Initialize the number of bribes needed to 0
    bribes_needed = 0

    # Loop through the candidates and calculate the number of bribes needed
    for i in range(1, n):
        if a[i] > 0:
            bribes_needed += min(a[i], votes_needed // (n - 1))

    # Return the number of bribes needed
    return bribes_needed

