
def solve(segments):
    # Sort the segments by their left endpoint
    sorted_segments = sorted(segments, key=lambda x: x[0])

    # Initialize the covering segment as the first segment
    covering_segment = sorted_segments[0]

    # Iterate through the remaining segments
    for segment in sorted_segments[1:]:
        # If the current segment is not covered by the covering segment, return -1
        if segment[0] < covering_segment[0] or segment[1] > covering_segment[1]:
            return -1

        # Otherwise, update the covering segment to be the current segment
        covering_segment = segment

    # If we reach this point, the covering segment covers all other segments, so return its number
    return covering_segment[2]

