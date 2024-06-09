
def solve(n, a):
    # Calculate the total number of votes
    total_votes = sum(a)

    # Initialize the minimum number of bribes as 0
    min_bribes = 0

    # Iterate through the array of votes
    for i in range(n):
        # Calculate the number of votes needed to win
        votes_needed = total_votes - a[i]

        # If Limak has enough votes to win, break the loop
        if votes_needed <= 0:
            break

        # Calculate the number of bribes needed
        bribes_needed = votes_needed // (n - i)

        # Update the minimum number of bribes
        min_bribes = max(min_bribes, bribes_needed)

    # Return the minimum number of bribes
    return min_bribes

