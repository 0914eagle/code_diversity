
def check_intersection(rect1, rect2):
    x1_min, y1_min, x1_max, y1_max = rect1
    x2_min, y2_min, x2_max, y2_max = rect2
    return not (x1_max <= x2_min or x2_max <= x1_min or y1_max <= y2_min or y2_max <= y1_min)

def find_intersection(rectangles):
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            if check_intersection(rectangles[i], rectangles[j]):
                return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    rectangles = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append((x1, y1, x2, y2))
    
    result = find_intersection(rectangles)
    print(result)
