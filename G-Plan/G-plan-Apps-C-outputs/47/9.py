
def rectangles_intersect(rectangles):
    def intersect(rect1, rect2):
        return not (rect2[0] >= rect1[2] or rect2[2] <= rect1[0] or rect2[1] >= rect1[3] or rect2[3] <= rect1[1])

    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if intersect(rectangles[i], rectangles[j]):
                return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(n)]
    print(rectangles_intersect(rectangles))
