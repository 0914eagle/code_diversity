
def parse_rectangles(corner_pairs):
    # Initialize an empty dictionary to store the rectangles
    rectangles = {}

    # Iterate through the corner pairs
    for i, (top_left, bottom_right) in enumerate(corner_pairs):
        # Check if the top-left corner is already in a rectangle
        if top_left in rectangles:
            # If it is, add the bottom-right corner to the same rectangle
            rectangles[top_left].append(bottom_right)
        else:
            # If it's not, create a new rectangle with the top-left and bottom-right corners
            rectangles[top_left] = [bottom_right]

    # Initialize an empty list to store the output
    output = []

    # Iterate through the rectangles
    for top_left, bottom_right_list in rectangles.items():
        # Check if the bottom-right corners are all in the same rectangle
        if all(bottom_right in rectangles for bottom_right in bottom_right_list):
            # If they are, add the index of the top-left corner to the output
            output.append(top_left)
        else:
            # If they're not, the input is invalid
            return "syntax error"

    return output

def main():
    # Read the number of corner pairs
    n = int(input())

    # Read the corner pairs
    corner_pairs = []
    for _ in range(n):
        r, c = map(int, input().split())
        corner_pairs.append((r, c))

    # Parse the rectangles
    output = parse_rectangles(corner_pairs)

    # Print the output
    for i in output:
        print(i)

if __name__ == '__main__':
    main()

