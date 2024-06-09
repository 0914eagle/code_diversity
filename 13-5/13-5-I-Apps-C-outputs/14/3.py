
def is_ghost_summoned(wire_length, points):
    # Initialize the wire as a list of booleans, with each index representing a point on the wire
    wire = [False] * (wire_length + 1)
    
    # Iterate through the points and mark the corresponding indices on the wire as True
    for point, direction in points:
        if direction == "C":
            wire[point] = True
        else:
            wire[wire_length - point] = True
    
    # Check if the wire touches itself at any point
    for i in range(wire_length):
        if wire[i] and wire[i + 1]:
            return "GHOST"
    
    return "SAFE"

def main():
    wire_length, num_points = map(int, input().split())
    points = []
    for _ in range(num_points):
        point, direction = input().split()
        points.append((int(point), direction))
    print(is_ghost_summoned(wire_length, points))

if __name__ == "__main__":
    main()

