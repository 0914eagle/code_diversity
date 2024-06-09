
def get_max_intersection_length(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the maximum length and the current length
    max_length = 0
    current_length = 0

    # Iterate through the segments
    for i in range(len(segments)):
        # Get the current segment
        segment = segments[i]

        # If the current segment is not nested within the previous segment
        if segment[0] >= current_length:
            # Update the current length
            current_length = segment[1]

            # Update the maximum length
            max_length = max(max_length, current_length)

    # Return the maximum length
    return max_length

