
def get_rows_and_columns(input_string):
    H, W = map(int, input_string.split())
    return H, W

def get_choosen_rows_and_columns(H, W):
    h, w = map(int, input().split())
    return h, w

def get_white_cells_remaining(H, W, h, w):
    return H*W - h*W - W*w + h*w

def main():
    H, W = get_rows_and_columns(input())
    h, w = get_choosen_rows_and_columns(H, W)
    print(get_white_cells_remaining(H, W, h, w))

if __name__ == '__main__':
    main()

