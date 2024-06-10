
def get_white_cells(H, W, h, w):
    return H * W - h * W - W * w + h * w

def main():
    H, W, h, w = map(int, input().split())
    print(get_white_cells(H, W, h, w))

if __name__ == '__main__':
    main()

