
def get_input():
    H, N, M = map(int, input().split())
    return H, N, M

def get_extra_bricks(H, N, M):
    total_bricks = N + M
    extra_2x2 = 0
    extra_4x2 = 0
    for i in range(1, H+1):
        width = 2*i
        if total_bricks >= width:
            total_bricks -= width
        else:
            if width % 2 == 0:
                extra_2x2 += width - total_bricks
            else:
                extra_4x2 += width - total_bricks
                extra_2x2 += 1
    return extra_2x2, extra_4x2

def solve(H, N, M):
    extra_2x2, extra_4x2 = get_extra_bricks(H, N, M)
    return extra_2x2, extra_4x2

if __name__ == '__main__':
    H, N, M = get_input()
    extra_2x2, extra_4x2 = solve(H, N, M)
    print(extra_2x2, extra_4x2)

