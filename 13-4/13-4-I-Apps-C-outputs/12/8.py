
def max_points(sequence):
    # Sort the sequence in descending order
    sequence.sort(reverse=True)
    # Initialize the maximum points and the current points
    max_points, current_points = 0, 0
    # Iterate through the sequence
    for i in range(len(sequence)):
        # Calculate the current points
        current_points += sequence[i]
        # Update the maximum points if necessary
        max_points = max(max_points, current_points)
        # If the current element is 1, break the loop
        if sequence[i] == 1:
            break
    return max_points

