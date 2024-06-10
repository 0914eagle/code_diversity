
def parse_corners(corners):
    # Initialize an empty dictionary to store the corner pairs
    corner_pairs = {}

    # Iterate through the list of corners
    for i, corner in enumerate(corners):
        # If the corner is a top-left corner, add it to the dictionary with its corresponding bottom-right corner
        if corner[0] == 1:
            corner_pairs[i] = corners[i + 1]
        # If the corner is a bottom-right corner, add it to the dictionary with its corresponding top-left corner
        else:
            corner_pairs[i] = corners[i - 1]

    # Initialize an empty list to store the parsed corners
    parsed_corners = []

    # Iterate through the dictionary of corner pairs
    for top_left, bottom_right in corner_pairs.items():
        # If the top-left corner is already in the parsed corners list, skip it
        if top_left in parsed_corners:
            continue
        # If the bottom-right corner is already in the parsed corners list, skip it
        if bottom_right in parsed_corners:
            continue
        # If the top-left corner and the bottom-right corner are not in the parsed corners list, add them to the list
        parsed_corners.append(top_left)
        parsed_corners.append(bottom_right)

    # Return the parsed corners list
    return parsed_corners

def main():
    # Read the number of corner pairs from stdin
    n = int(input())

    # Read the corner pairs from stdin
    corners = []
    for _ in range(n):
        r, c = map(int, input().split())
        corners.append((r, c))

    # Parse the corners
    parsed_corners = parse_corners(corners)

    # Print the parsed corners
    for corner in parsed_corners:
        print(corner)

if __name__ == '__main__':
    main()

