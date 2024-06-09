
def solve(arr, segments):
    # Sort the segments by their length in descending order
    segments.sort(key=lambda x: x[1] - x[0], reverse=True)

    # Initialize the maximum difference and the chosen segments
    max_diff = 0
    chosen_segments = []

    # Iterate over the segments
    for segment in segments:
        # Get the start and end indices of the segment
        start, end = segment[0], segment[1]

        # Decrease the values of the segment by 1
        for i in range(start, end):
            arr[i] -= 1

        # Calculate the difference between the maximum and minimum values in the array
        diff = max(arr) - min(arr)

        # If the difference is greater than the current maximum difference, update the maximum difference and the chosen segments
        if diff > max_diff:
            max_diff = diff
            chosen_segments = [segment]
        # If the difference is equal to the current maximum difference, add the segment to the list of chosen segments
        elif diff == max_diff:
            chosen_segments.append(segment)

    # Return the maximum difference and the list of chosen segments
    return max_diff, chosen_segments

