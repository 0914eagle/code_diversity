
def f1(L, n):
    # function to check if the wire will touch itself
    def check_touch(point, direction):
        if direction == "C":
            return point >= L - point
        else:
            return point <= L - point
    
    # function to check if the wire ghost will appear
    def check_ghost(points, directions):
        for i in range(n):
            if check_touch(points[i], directions[i]):
                return "GHOST"
        return "SAFE"
    
    # main function
    points = []
    directions = []
    for i in range(n):
        point, direction = map(int, input().split())
        points.append(point)
        directions.append(direction)
    return check_ghost(points, directions)

def f2(L, n):
    # function to check if the wire will touch itself
    def check_touch(point, direction):
        if direction == "C":
            return point >= L - point
        else:
            return point <= L - point
    
    # function to check if the wire ghost will appear
    def check_ghost(points, directions):
        for i in range(n):
            if check_touch(points[i], directions[i]):
                return "GHOST"
        return "SAFE"
    
    # main function
    points = []
    directions = []
    for i in range(n):
        point, direction = map(int, input().split())
        points.append(point)
        directions.append(direction)
    return check_ghost(points, directions)

if __name__ == '__main__':
    L, n = map(int, input().split())
    print(f1(L, n))

