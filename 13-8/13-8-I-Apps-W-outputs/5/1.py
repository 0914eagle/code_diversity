
def find_covering_segment(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the covering segment as the first segment
    covering_segment = segments[0]

    # Iterate through the remaining segments
    for segment in segments[1:]:
        # Check if the current segment covers the covering segment
        if covering_segment[0] <= segment[0] and covering_segment[1] >= segment[1]:
            # If it does, update the covering segment
            covering_segment = segment
        else:
            # If it doesn't, return -1 as there is no covering segment
            return -1

    # Return the number of the covering segment
    return segments.index(covering_segment) + 1

