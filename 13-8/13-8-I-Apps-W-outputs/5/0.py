
def solve(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the covering segment to be the first segment
    covering_segment = segments[0]

    # Iterate through the remaining segments
    for segment in segments[1:]:
        # If the current segment is not covered by the covering segment, return -1
        if segment[0] < covering_segment[0] or segment[1] > covering_segment[1]:
            return -1

        # Update the covering segment to be the current segment if it is larger than the current covering segment
        if segment[1] > covering_segment[1]:
            covering_segment = segment

    # Return the number of the covering segment
    return segments.index(covering_segment) + 1

