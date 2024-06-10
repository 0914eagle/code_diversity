
def get_input():
    return [int(x) for x in input().split()]

def paint_cells(h, w, H, W):
    return H * W - h * W - w * H + h * w

def main():
    H, W = get_input()
    h, w = get_input()
    print(paint_cells(h, w, H, W))

if __name__ == '__main__':
    main()

