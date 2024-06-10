
def get_box_size(N):
    # Find the smallest box size that can fit all the widgets
    for W in range(1, int(N**0.5) + 1):
        H = N // W
        if H % 2 == 1:
            H += 1
        if W <= 2 * H:
            return W, H
    return 0, 0

def get_empty_squares(W, H):
    # Calculate the number of empty squares in the box
    return (W - N) * (H - N)

def solve(N):
    W, H = get_box_size(N)
    return get_empty_squares(W, H)

if __name__ == '__main__':
    N = int(input())
    print(solve(N))

