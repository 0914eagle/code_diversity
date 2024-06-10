
def get_input():
    return list(map(int, input().split()))

def get_number_of_white_cells(H, W, h, w):
    return H * W - h * W - W * w + h * w

def main():
    H, W, h, w = get_input()
    print(get_number_of_white_cells(H, W, h, w))

if __name__ == '__main__':
    main()

