
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    # print(stars)
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            if x1 == x2 and y1 == y2:
                return "-1"
            if x1 == x2 or y1 == y2:
                continue
            if x1 < x2 and y1 < y2:
                if x2 - x1 == y2 - y1:
                    stars[i] = (x1, y1, x2 - x1)
                    stars[j] = (x2, y2, x2 - x1)
                    break
            if x1 > x2 and y1 > y2:
                if x1 - x2 == y1 - y2:
                    stars[i] = (x1, y1, x1 - x2)
                    stars[j] = (x2, y2, x1 - x2)
                    break
    return str(len(stars)) + "\n" + "\n".join([f"{s[0]} {s[1]} {s[2]}" for s in stars])

