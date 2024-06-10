
def cut_glass(w, h, n, cuts):
    # Initialize the maximum area and the current fragment
    max_area = 0
    fragment = [w, h]

    # Loop through each cut
    for cut in cuts:
        # If the cut is horizontal, find the maximum area of the fragment below the cut
        if cut[0] == "H":
            max_area = max(max_area, fragment[0] * cut[1])
        # If the cut is vertical, find the maximum area of the fragment to the left of the cut
        elif cut[0] == "V":
            max_area = max(max_area, fragment[1] * cut[1])

        # Update the current fragment based on the cut
        if cut[0] == "H":
            fragment[1] = cut[1]
        elif cut[0] == "V":
            fragment[0] = cut[1]

    # Return the maximum area
    return max_area

def main():
    w, h, n = map(int, input().split())
    cuts = []
    for _ in range(n):
        cuts.append(input().split())
    print(cut_glass(w, h, n, cuts))

if __name__ == '__main__':
    main()

