
def get_max_fragment_area(glass_sheet, cuts):
    # Initialize variables
    max_area = 0
    current_area = 0
    x1, y1, x2, y2 = 0, 0, 0, 0

    # Loop through each cut
    for cut in cuts:
        # Get the coordinates of the current cut
        x, y = cut

        # Check if the current cut is horizontal or vertical
        if x != 0:
            # Horizontal cut
            x1, x2 = x, x
            y1, y2 = 0, glass_sheet[1]
        else:
            # Vertical cut
            x1, x2 = 0, glass_sheet[0]
            y1, y2 = y, y

        # Calculate the area of the current cut
        current_area = (x2 - x1) * (y2 - y1)

        # Check if the current area is greater than the maximum area
        if current_area > max_area:
            max_area = current_area

    # Return the maximum area
    return max_area

def get_cuts(glass_sheet, n):
    # Initialize variables
    cuts = []
    x, y = 0, 0

    # Loop through each cut
    for i in range(n):
        # Get the coordinates of the current cut
        x, y = map(int, input().split())

        # Check if the current cut is horizontal or vertical
        if x != 0:
            # Horizontal cut
            x1, x2 = x, x
            y1, y2 = 0, glass_sheet[1]
        else:
            # Vertical cut
            x1, x2 = 0, glass_sheet[0]
            y1, y2 = y, y

        # Add the current cut to the list of cuts
        cuts.append((x1, y1, x2, y2))

    # Return the list of cuts
    return cuts

def main():
    # Read the input
    glass_sheet = tuple(map(int, input().split()))
    n = int(input())

    # Get the list of cuts
    cuts = get_cuts(glass_sheet, n)

    # Get the maximum fragment area
    max_area = get_max_fragment_area(glass_sheet, cuts)

    # Print the result
    print(max_area)

if __name__ == '__main__':
    main()

