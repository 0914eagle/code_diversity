
def solve(n, a):
    # Find the candidate with the most votes
    max_votes = max(a)
    max_index = a.index(max_votes)

    # Initialize the number of bribes needed to 0
    bribes_needed = 0

    # Loop through the candidates and check if they have more votes than Limak
    for i in range(1, n):
        if a[i] > a[0]:
            # Calculate the number of bribes needed to overtake the current candidate
            bribes_needed += a[i] - a[0]

    # Return the minimum number of bribes needed to win the election
    return bribes_needed

