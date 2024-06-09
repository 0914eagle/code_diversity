
def f1(L, n, points):
    # Initialize a list to store the positions of the wire
    positions = [0]
    # Iterate through the points and directions
    for point, direction in points:
        # Check if the wire will touch itself
        if direction == "C" and point in positions:
            return "GHOST"
        # Add the position of the wire to the list
        positions.append(point)
    return "SAFE"

def f2(L, n, points):
    # Initialize a set to store the positions of the wire
    positions = set([0])
    # Iterate through the points and directions
    for point, direction in points:
        # Check if the wire will touch itself
        if direction == "C" and point in positions:
            return "GHOST"
        # Add the position of the wire to the set
        positions.add(point)
    return "SAFE"

if __name__ == '__main__':
    L, n = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(f1(L, n, points))
    print(f2(L, n, points))

