
def get_max_intersection_length(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the maximum length and the segment to remove
    max_length = 0
    segment_to_remove = None

    # Iterate over the segments
    for i in range(len(segments)):
        # Get the current segment
        segment = segments[i]

        # Check if the segment is degenerate (i.e., a point)
        if segment[0] == segment[1]:
            continue

        # Initialize the intersection length and the previous segment
        intersection_length = 0
        previous_segment = None

        # Iterate over the remaining segments
        for j in range(i + 1, len(segments)):
            # Get the current segment
            current_segment = segments[j]

            # Check if the segments intersect
            if segment[1] >= current_segment[0] and segment[0] <= current_segment[1]:
                # Calculate the intersection length
                intersection_length = max(intersection_length, current_segment[1] - current_segment[0])

                # Update the previous segment
                previous_segment = current_segment

        # Check if the intersection length is greater than the current maximum
        if intersection_length > max_length:
            # Update the maximum length and the segment to remove
            max_length = intersection_length
            segment_to_remove = segment

    # Return the maximum length
    return max_length
