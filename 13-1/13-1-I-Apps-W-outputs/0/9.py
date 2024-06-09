
def get_max_segments(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the maximum number of segments in the union as 0
    max_segments = 0

    # Iterate through the segments
    for i in range(len(segments)):
        # Initialize the current segment as the first segment
        current_segment = segments[i]

        # Initialize the number of segments in the union as 1
        num_segments = 1

        # Iterate through the remaining segments
        for j in range(i+1, len(segments)):
            # Check if the current segment and the next segment intersect
            if current_segment[1] >= segments[j][0]:
                # If they intersect, merge them into a single segment
                current_segment = [current_segment[0], max(current_segment[1], segments[j][1])]
                num_segments += 1

        # Update the maximum number of segments in the union if necessary
        max_segments = max(max_segments, num_segments)

    return max_segments

