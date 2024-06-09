
def is_ghost_appeared(wire_length, bend_points):
    # Initialize the wire as a list of zeros and ones, with zeros representing the straight part of the wire and ones representing the curved part
    wire = [0] * (wire_length + 1)
    
    # Iterate through the bend points and mark the corresponding part of the wire as curved
    for point, direction in bend_points:
        if direction == "C":
            wire[point] = 1
            wire[point + 1] = 1
        else:
            wire[point] = 1
            wire[point - 1] = 1
    
    # Check if the wire has touched itself at any point
    for i in range(wire_length):
        if wire[i] == 1 and wire[i + 1] == 1:
            return "GHOST"
    
    return "SAFE"

def main():
    wire_length, num_bend_points = map(int, input().split())
    bend_points = []
    for _ in range(num_bend_points):
        point, direction = map(int, input().split())
        bend_points.append((point, direction))
    print(is_ghost_appeared(wire_length, bend_points))

if __name__ == "__main__":
    main()

