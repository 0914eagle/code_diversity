
def solve(segments):
    # Sort the segments by their left endpoint
    segments.sort(key=lambda x: x[0])

    # Initialize the coverage array with False
    coverage = [False] * len(segments)

    # Loop through the segments and check if they cover any other segment
    for i, segment in enumerate(segments):
        for j in range(i+1, len(segments)):
            if segments[j][0] <= segment[0] and segments[j][1] >= segment[1]:
                coverage[i] = True
                break

    # Check if there is a segment that covers all other segments
    for i, segment in enumerate(segments):
        if coverage[i] and all(coverage[j] for j in range(len(segments)) if j != i):
            return i+1

    # If no such segment exists, return -1
    return -1

