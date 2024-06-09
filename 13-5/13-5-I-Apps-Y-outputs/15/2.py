
def get_input():
    H, N, M = map(int, input().split())
    return H, N, M

def get_extra_bricks(H, N, M):
    extra_2x2 = 0
    extra_4x2 = 0
    for i in range(1, H+1):
        if i % 2 == 0:
            extra_2x2 += 1
        else:
            extra_4x2 += 1
    return extra_2x2 + N, extra_4x2 + M

def solve(H, N, M):
    extra_2x2, extra_4x2 = get_extra_bricks(H, N, M)
    return extra_2x2, extra_4x2

if __name__ == '__main__':
    H, N, M = get_input()
    extra_2x2, extra_4x2 = solve(H, N, M)
    print(extra_2x2, extra_4x2)

