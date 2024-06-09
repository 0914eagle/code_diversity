
def f1(L, n):
    # function to check if the wire will touch itself
    def check_touch(points):
        for i in range(n - 1):
            for j in range(i + 1, n):
                if points[i] == points[j] or abs(points[i] - points[j]) == L:
                    return True
        return False
    
    # function to get the new position of the point after bending
    def get_new_position(point, direction):
        if direction == "C":
            return (point - 1) % L
        else:
            return (point + 1) % L
    
    # function to check if the wire ghost will appear
    def check_ghost(points):
        for i in range(n - 1):
            for j in range(i + 1, n):
                if points[i] == points[j] or abs(points[i] - points[j]) == L:
                    return True
        return False
    
    # main function
    points = []
    for i in range(n):
        point, direction = map(int, input().split())
        points.append(point)
    
    # sort the points in ascending order
    points.sort()
    
    # check if the wire will touch itself
    if check_touch(points):
        return "GHOST"
    
    # get the new position of each point after bending
    new_points = [get_new_position(point, direction) for point, direction in zip(points, directions)]
    
    # check if the wire ghost will appear
    if check_ghost(new_points):
        return "GHOST"
    
    return "SAFE"

def f2(...):
    # function 2 code here
    pass

if __name__ == '__main__':
    L, n = map(int, input().split())
    print(f1(L, n))

