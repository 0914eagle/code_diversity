
def get_white_region(rectangle):
    
    x1, y1 = rectangle[0]
    x2, y2 = rectangle[1]
    return (x2 - x1) * (y2 - y1)

def main():
    W, H, N = map(int, input().split())
    rectangle = [(0, 0), (W, 0), (W, H), (0, H)]
    for _ in range(N):
        x, y, a = map(int, input().split())
        if a == 1:
            rectangle[0] = (x, y)
        elif a == 2:
            rectangle[1] = (x, y)
        elif a == 3:
            rectangle[2] = (x, y)
        elif a == 4:
            rectangle[3] = (x, y)
    print(get_white_region(rectangle))

if __name__ == '__main__':
    main()

