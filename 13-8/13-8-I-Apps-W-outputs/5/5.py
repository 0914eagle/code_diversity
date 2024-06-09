
def solve(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the coverage array with False values
    coverage = [False] * len(segments)

    # Loop through the segments and mark the segments that are covered
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            if segments[i][0] <= segments[j][0] and segments[j][1] <= segments[i][1]:
                coverage[j] = True

    # Return the index of the first segment that is not covered
    for i in range(len(coverage)):
        if not coverage[i]:
            return i + 1

    # If all segments are covered, return -1
    return -1

