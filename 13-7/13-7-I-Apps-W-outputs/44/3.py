
def cut_glass(w, h, n, cuts):
    # Initialize the maximum area and the current fragment
    max_area = 0
    current_fragment = [w, h]

    # Loop through each cut
    for cut in cuts:
        # Get the x and y coordinates of the cut
        x, y = cut

        # Check if the cut is horizontal or vertical
        if x == -1:
            # Horizontal cut
            current_fragment[1] = y
        else:
            # Vertical cut
            current_fragment[0] = x

        # Calculate the area of the current fragment
        area = current_fragment[0] * current_fragment[1]

        # Update the maximum area if necessary
        if area > max_area:
            max_area = area

    # Return the maximum area
    return max_area

def main():
    w, h, n = map(int, input().split())
    cuts = []
    for i in range(n):
        x, y = map(int, input().split())
        cuts.append([x, y])
    print(cut_glass(w, h, n, cuts))

if __name__ == '__main__':
    main()

