
def get_white_region_area(W, H, N, x_coords, y_coords, a_seq):
    white_region = [[True] * W for _ in range(H)]
    for i in range(N):
        x, y = x_coords[i], y_coords[i]
        if a_seq[i] == 1:
            for j in range(W):
                if j < x:
                    white_region[y][j] = False
        elif a_seq[i] == 2:
            for j in range(W):
                if j > x:
                    white_region[y][j] = False
        elif a_seq[i] == 3:
            for j in range(H):
                if j < y:
                    white_region[j][x] = False
        else:
            for j in range(H):
                if j > y:
                    white_region[j][x] = False
    return sum(sum(row) for row in white_region)

def main():
    W, H, N = map(int, input().split())
    x_coords = []
    y_coords = []
    a_seq = []
    for i in range(N):
        x, y, a = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)
        a_seq.append(a)
    print(get_white_region_area(W, H, N, x_coords, y_coords, a_seq))

if __name__ == '__main__':
    main()

