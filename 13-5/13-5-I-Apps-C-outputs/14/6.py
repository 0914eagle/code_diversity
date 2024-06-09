
def f1(L, n):
    # function to check if the wire will touch itself
    def will_touch_itself(points, direction):
        for i in range(len(points)):
            if points[i] in points[i+1:]:
                return True
        return False

    # function to determine the direction of the bend
    def determine_direction(point, direction):
        if direction == "C":
            return "CCW"
        else:
            return "CW"

    # function to bend the wire
    def bend_wire(points, direction):
        bended_wire = []
        for point in points:
            bended_wire.append(point)
        return bended_wire

    # function to check if the wire ghost appears
    def check_wire_ghost(bended_wire):
        for i in range(len(bended_wire)):
            if bended_wire[i] in bended_wire[i+1:]:
                return "GHOST"
        return "SAFE"

    # main function
    points = []
    direction = []
    for i in range(n):
        points.append(int(input()))
        direction.append(input())
    bended_wire = bend_wire(points, direction)
    return check_wire_ghost(bended_wire)

def f2(L, n):
    # function to check if the wire will touch itself
    def will_touch_itself(points, direction):
        for i in range(len(points)):
            if points[i] in points[i+1:]:
                return True
        return False

    # function to determine the direction of the bend
    def determine_direction(point, direction):
        if direction == "C":
            return "CCW"
        else:
            return "CW"

    # function to bend the wire
    def bend_wire(points, direction):
        bended_wire = []
        for point in points:
            bended_wire.append(point)
        return bended_wire

    # function to check if the wire ghost appears
    def check_wire_ghost(bended_wire):
        for i in range(len(bended_wire)):
            if bended_wire[i] in bended_wire[i+1:]:
                return "GHOST"
        return "SAFE"

    # main function
    points = []
    direction = []
    for i in range(n):
        points.append(int(input()))
        direction.append(input())
    bended_wire = bend_wire(points, direction)
    return check_wire_ghost(bended_wire)

if __name__ == '__main__':
    L, n = map(int, input().split())
    print(f1(L, n))
    print(f2(L, n))

