
def get_remaining_cells(H, W, h, w):
    return H * W - h * W - H * w + h * w

def main():
    H, W, h, w = map(int, input().split())
    print(get_remaining_cells(H, W, h, w))

if __name__ == '__main__':
    main()

