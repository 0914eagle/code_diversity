
def get_black_rectangles(n, m):
    black_rectangles = []
    for i in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        black_rectangles.append((x1, y1, x2, y2))
    return black_rectangles

def get_white_cells(n, m, black_rectangles):
    white_cells = set()
    for x1, y1, x2, y2 in black_rectangles:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                white_cells.add((x, y))
    return white_cells

def get_cost(n, m, black_rectangles, white_cells):
    cost = 0
    for x1, y1, x2, y2 in black_rectangles:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x, y) in white_cells:
                    cost += 1
    return cost

def main():
    n, m = map(int, input().split())
    black_rectangles = get_black_rectangles(n, m)
    white_cells = get_white_cells(n, m, black_rectangles)
    cost = get_cost(n, m, black_rectangles, white_cells)
    print(cost)

if __name__ == '__main__':
    main()

