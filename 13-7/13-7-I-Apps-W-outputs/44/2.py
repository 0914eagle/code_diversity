
def cut_glass(w, h, n, cuts):
    # Initialize the maximum area and the current fragment
    max_area = 0
    current_fragment = [w, h]

    # Loop through each cut
    for cut in cuts:
        # If the cut is horizontal, find the area of the fragment to the left and right of the cut
        if cut[0] == 'H':
            left_area = current_fragment[0] * cut[1]
            right_area = (w - cut[1]) * current_fragment[1]

        # If the cut is vertical, find the area of the fragment above and below the cut
        else:
            above_area = current_fragment[1] * cut[1]
            below_area = (h - cut[1]) * current_fragment[0]

        # Find the maximum area of the two fragments
        max_area = max(left_area, right_area, above_area, below_area)

        # Update the current fragment to the largest of the two fragments
        if max_area == left_area:
            current_fragment = [cut[1], current_fragment[1]]
        elif max_area == right_area:
            current_fragment = [w - cut[1], current_fragment[1]]
        elif max_area == above_area:
            current_fragment = [current_fragment[0], cut[1]]
        else:
            current_fragment = [current_fragment[0], h - cut[1]]

    # Return the maximum area
    return max_area

def main():
    w, h, n = map(int, input().split())
    cuts = []
    for i in range(n):
        cut = input()
        cuts.append(tuple(map(int, cut.split())))
    print(cut_glass(w, h, n, cuts))

if __name__ == '__main__':
    main()

