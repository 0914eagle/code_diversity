
def check_intersection(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    return not (x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1)

def find_intersecting_rectangles(rectangles):
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            if check_intersection(rectangles[i], rectangles[j]):
                return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(n)]
    print(find_intersecting_rectangles(rectangles))
