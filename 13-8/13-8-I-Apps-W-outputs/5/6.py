
def solve(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the cover segment as the first segment
    cover_segment = segments[0]

    # Iterate through the remaining segments
    for segment in segments[1:]:
        # Check if the current segment is covered by the cover segment
        if cover_segment[0] <= segment[0] and cover_segment[1] >= segment[1]:
            # If it is, update the cover segment
            cover_segment = segment
        else:
            # If it's not, return -1 as there is no cover segment
            return -1

    # Return the number of the cover segment
    return segments.index(cover_segment) + 1

