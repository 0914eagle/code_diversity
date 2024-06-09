
def f1(L, n):
    # function to check if the wire will touch itself
    def check_touch(point, direction):
        if direction == "C":
            return point >= L - point
        else:
            return point <= L - point
    
    # function to check if the wire will touch itself at any point
    def check_touch_any(points, directions):
        for point, direction in zip(points, directions):
            if check_touch(point, direction):
                return True
        return False
    
    # function to check if the wire will touch itself at any point during the bending process
    def check_touch_bending(points, directions):
        for i in range(1, len(points)):
            if check_touch(points[i] - points[i - 1], directions[i - 1]):
                return True
        return False
    
    # main function
    return "GHOST" if check_touch_bending(points, directions) else "SAFE"

def f2(L, n):
    # function to get the points and directions from the input
    points = []
    directions = []
    for i in range(n):
        point, direction = map(int, input().split())
        points.append(point)
        directions.append(direction)
    
    # function to call f1 and print the output
    output = f1(L, n, points, directions)
    print(output)

if __name__ == '__main__':
    L, n = map(int, input().split())
    f2(L, n)

