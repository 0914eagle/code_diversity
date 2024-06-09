
def solve(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the cover segment to be the first segment
    cover_segment = segments[0]

    # Iterate through the remaining segments
    for segment in segments[1:]:
        # If the current segment does not overlap with the cover segment, return -1
        if segment[0] > cover_segment[1]:
            return -1
        # Update the cover segment to be the maximum segment that covers all previous segments
        cover_segment = [cover_segment[0], max(cover_segment[1], segment[1])]

    # Return the number of the cover segment
    return segments.index(cover_segment) + 1

