
def cut_glass(w, h, n):
    # Initialize the variables
    glass = [[0] * (w + 1) for _ in range(h + 1)]
    max_area = 0
    result = []

    # Loop through each cut
    for i in range(n):
        # Read the next cut from stdin
        cut = input().split()

        # Get the coordinates of the cut
        if cut[0] == "H":
            x1, y1, x2, y2 = 0, int(cut[1]), w, int(cut[1])
        else:
            x1, y1, x2, y2 = int(cut[1]), 0, int(cut[1]), h

        # Update the glass matrix
        for j in range(y1, y2 + 1):
            for k in range(x1, x2 + 1):
                glass[j][k] += 1

        # Find the maximum area
        max_area = max(max_area, max(map(max, glass)))
        result.append(max_area)

    return result

def main():
    w, h, n = map(int, input().split())
    result = cut_glass(w, h, n)
    for area in result:
        print(area)

if __name__ == '__main__':
    main()

