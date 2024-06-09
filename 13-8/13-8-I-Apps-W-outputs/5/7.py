
def solve(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the coverage set with the first segment
    coverage = set([segments[0]])

    # Iterate through the remaining segments
    for segment in segments[1:]:
        # Check if the segment is covered by the coverage set
        covered = False
        for covered_segment in coverage:
            if segment[0] <= covered_segment[0] and segment[1] >= covered_segment[1]:
                covered = True
                break

        # If the segment is not covered, add it to the coverage set
        if not covered:
            coverage.add(segment)

    # Check if all segments are covered
    if len(coverage) == len(segments):
        return 1
    else:
        return -1

