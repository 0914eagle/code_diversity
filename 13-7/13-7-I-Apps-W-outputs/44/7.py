
def cut_glass(w, h, n, cuts):
    # Initialize the maximum area and the current fragment
    max_area = 0
    fragment = [w, h]

    # Loop through each cut
    for cut in cuts:
        # If the cut is horizontal, cut the fragment horizontally and find the maximum area
        if cut[0] == "H":
            fragment = horizontal_cut(fragment, cut[1])
            max_area = max(max_area, get_area(fragment))
        # If the cut is vertical, cut the fragment vertically and find the maximum area
        else:
            fragment = vertical_cut(fragment, cut[1])
            max_area = max(max_area, get_area(fragment))

    # Return the maximum area
    return max_area

def horizontal_cut(fragment, y):
    # Cut the fragment horizontally at the given distance from the lower edge
    return [fragment[0], fragment[1] - y]

def vertical_cut(fragment, x):
    # Cut the fragment vertically at the given distance from the left edge
    return [fragment[0] - x, fragment[1]]

def get_area(fragment):
    # Return the area of the fragment
    return fragment[0] * fragment[1]

def main():
    w, h, n = map(int, input().split())
    cuts = []
    for _ in range(n):
        cuts.append(input().split())
    print(cut_glass(w, h, n, cuts))

if __name__ == '__main__':
    main()

