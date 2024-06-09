
def solve(n, a):
    # Calculate the number of votes Limak needs to have strictly more than any other candidate
    votes_needed = max(a) + 1

    # Initialize a counter for the number of citizens Limak needs to bribe
    citizens_needed = 0

    # Iterate through the array of votes for each candidate
    for i in range(n):
        # If the current candidate has fewer votes than what Limak needs,
        # increment the counter by the difference between the two
        if a[i] < votes_needed:
            citizens_needed += votes_needed - a[i]

    return citizens_needed

