
def get_input():
    H, N, M = map(int, input().split())
    return H, N, M

def get_extra_bricks(H, N, M):
    total_bricks = N + M
    extra_bricks = 0
    for i in range(1, H+1):
        width = 2*i
        needed_bricks = width * i
        if total_bricks < needed_bricks:
            extra_bricks += needed_bricks - total_bricks
    return extra_bricks

def get_extra_2x2_bricks(H, N, M):
    total_bricks = N + M
    extra_2x2_bricks = 0
    for i in range(1, H+1):
        width = 2*i
        needed_bricks = width * i
        if total_bricks < needed_bricks:
            extra_2x2_bricks += needed_bricks - total_bricks
    return extra_2x2_bricks

def get_extra_4x2_bricks(H, N, M):
    total_bricks = N + M
    extra_4x2_bricks = 0
    for i in range(1, H+1):
        width = 2*i
        needed_bricks = width * i
        if total_bricks < needed_bricks:
            extra_4x2_bricks += needed_bricks - total_bricks
    return extra_4x2_bricks

def get_min_extra_bricks(H, N, M):
    total_bricks = N + M
    min_extra_bricks = total_bricks
    for i in range(1, H+1):
        width = 2*i
        needed_bricks = width * i
        if total_bricks < needed_bricks:
            min_extra_bricks = min(min_extra_bricks, needed_bricks - total_bricks)
    return min_extra_bricks

def get_optimal_solution(H, N, M):
    total_bricks = N + M
    optimal_solution = (0, 0)
    for i in range(1, H+1):
        width = 2*i
        needed_bricks = width * i
        if total_bricks < needed_bricks:
            extra_bricks = needed_bricks - total_bricks
            extra_2x2_bricks = extra_bricks // 2
            extra_4x2_bricks = extra_bricks % 2
            if extra_2x2_bricks + extra_4x2_bricks < optimal_solution[0] + optimal_solution[1]:
                optimal_solution = (extra_2x2_bricks, extra_4x2_bricks)
    return optimal_solution

def main():
    H, N, M = get_input()
    extra_bricks = get_extra_bricks(H, N, M)
    extra_2x2_bricks = get_extra_2x2_bricks(H, N, M)
    extra_4x2_bricks = get_extra_4x2_bricks(H, N, M)
    min_extra_bricks = get_min_extra_bricks(H, N, M)
    optimal_solution = get_optimal_solution(H, N, M)
    print(f"Total bricks: {extra_bricks}")
    print(f"Total 2x2 bricks: {extra_2x2_bricks}")
    print(f"Total 4x2 bricks: {extra_4x2_bricks}")
    print(f"Minimum extra bricks: {min_extra_bricks}")
    print(f"Optimal solution: {optimal_solution}")

if __name__ == '__main__':
    main()

