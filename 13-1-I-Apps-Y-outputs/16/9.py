
def solve(N, M, A):
    # Sort the list of votes in descending order
    A.sort(reverse=True)
    # Initialize a variable to keep track of the total number of votes
    total_votes = sum(A)
    # Initialize a variable to keep track of the number of popular items selected
    num_popular_items = 0
    # Iterate through the list of votes
    for vote in A:
        # Check if the current vote is greater than or equal to the minimum threshold
        if vote >= total_votes / (4 * M):
            # Increment the number of popular items selected
            num_popular_items += 1
        # Check if the maximum number of popular items has been selected
        if num_popular_items == M:
            # Return 'Yes' to indicate that M popular items can be selected
            return "Yes"
    # Return 'No' to indicate that M popular items cannot be selected
    return "No"

