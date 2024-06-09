
def max_fragment_area(w, h, n, cuts):
    # Initialize the maximum area and the current area
    max_area = 0
    current_area = w * h

    # Loop through each cut
    for cut in cuts:
        # If the cut is horizontal, calculate the area of the fragment to the left and right of the cut
        if cut[0] == "H":
            left_area = (cut[1] * h)
            right_area = (w - cut[1]) * h
        # If the cut is vertical, calculate the area of the fragment above and below the cut
        else:
            above_area = (cut[1] * w)
            below_area = (h - cut[1]) * w

        # Calculate the maximum area of the current fragment
        current_area = max(left_area, right_area, above_area, below_area)

        # Update the maximum area if necessary
        if current_area > max_area:
            max_area = current_area

    # Return the maximum area
    return max_area

# Main
w, h, n = map(int, input().split())
cuts = []
for i in range(n):
    cut = input()
    cuts.append(cut)

print(max_fragment_area(w, h, n, cuts))

