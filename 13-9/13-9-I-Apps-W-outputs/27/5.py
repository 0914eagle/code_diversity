
def solve(n, arr):
    # Calculate the total number of votes
    total_votes = sum(arr)

    # Initialize a variable to store the minimum number of citizens to bribe
    min_citizens = 0

    # Iterate through the array of votes
    for i in range(n):
        # Calculate the number of votes Limak needs to have strictly more than the current candidate
        needed_votes = total_votes - arr[i] + 1

        # If Limak has enough votes, break the loop
        if needed_votes <= 0:
            break

        # Calculate the number of citizens Limak needs to bribe to achieve the needed votes
        citizens_needed = needed_votes // arr[i]

        # Update the minimum number of citizens to bribe
        min_citizens += citizens_needed

    # Return the minimum number of citizens to bribe
    return min_citizens

