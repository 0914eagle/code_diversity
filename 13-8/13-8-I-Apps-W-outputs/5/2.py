
def solve(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the covered segments as an empty set
    covered_segments = set()

    # Iterate through the segments
    for segment in segments:
        # If the current segment is covered by any other segment, skip it
        if any(segment[0] in covered_segment for covered_segment in covered_segments):
            continue

        # If the current segment covers all other segments, return its number
        if all(segment[0] <= other_segment[0] and segment[1] >= other_segment[1] for other_segment in segments):
            return segment[2]

        # Otherwise, add the current segment to the covered segments set
        covered_segments.add(segment)

    # If no segment covers all other segments, return -1
    return -1

