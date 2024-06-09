
def get_max_fragment_area(glass_sheet, cuts):
    # Initialize variables
    max_area = 0
    current_area = glass_sheet[0] * glass_sheet[1]

    # Loop through each cut
    for cut in cuts:
        # Get the coordinates of the cut
        x, y = cut

        # Check if the cut is horizontal or vertical
        if x == -1:
            # Horizontal cut
            current_area = glass_sheet[1] * (glass_sheet[0] - x)
        else:
            # Vertical cut
            current_area = glass_sheet[0] * (glass_sheet[1] - y)

        # Update the maximum area
        max_area = max(max_area, current_area)

    # Return the maximum area
    return max_area

