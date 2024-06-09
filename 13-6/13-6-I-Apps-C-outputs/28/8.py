
def f1(n, rectangles):
    # find the common point
    common_point = None
    for i in range(n):
        for j in range(i+1, n):
            if rectangles[i].intersects(rectangles[j]):
                common_point = rectangles[i].intersection(rectangles[j])
                break
        if common_point:
            break
    
    # check if the common point is inside at least (n-1) rectangles
    count = 0
    for i in range(n):
        if rectangles[i].contains(common_point):
            count += 1
        if count == n-1:
            return common_point
    
    # if no common point is found, return None
    return None

def f2(n, rectangles):
    # find the common point
    common_point = None
    for i in range(n):
        for j in range(i+1, n):
            if rectangles[i].intersects(rectangles[j]):
                common_point = rectangles[i].intersection(rectangles[j])
                break
        if common_point:
            break
    
    # check if the common point is inside at least (n-1) rectangles
    count = 0
    for i in range(n):
        if rectangles[i].contains(common_point):
            count += 1
        if count == n-1:
            return common_point
    
    # if no common point is found, return None
    return None

def main():
    n = int(input())
    rectangles = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append(Rectangle(x1, y1, x2, y2))
    
    common_point = f1(n, rectangles)
    if common_point:
        print(common_point.x, common_point.y)
    else:
        print(-1, -1)

if __name__ == '__main__':
    main()

