
def is_safe_bending(wire_length, points):
    # Initialize a list to store the bends
    bends = []

    # Iterate through the points and append the bends to the list
    for point, direction in points:
        if direction == "C":
            bends.append((point, "C"))
        else:
            bends.append((point, "W"))

    # Sort the bends by their position on the wire
    bends.sort(key=lambda x: x[0])

    # Iterate through the bends and check if they form a loop
    for i in range(len(bends)):
        for j in range(i+1, len(bends)):
            if bends[i][0] == bends[j][0]:
                return "GHOST"
            if bends[i][1] == bends[j][1] and abs(bends[i][0] - bends[j][0]) == wire_length - 1:
                return "GHOST"

    return "SAFE"

