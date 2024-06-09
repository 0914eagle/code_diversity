
def solve(n, rectangles):
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, x2, y2 = rectangles[i]
            x3, y3, x4, y4 = rectangles[j]
            if x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4:
                if y1 <= y3 <= y2 or y1 <= y4 <= y2 or y3 <= y1 <= y4 or y3 <= y2 <= y4:
                    return 1
    return 0

