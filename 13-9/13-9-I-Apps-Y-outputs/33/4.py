
def get_input():
    N = int(input())
    H = list(map(int, input().split()))
    return N, H

def solve(N, H):
    max_moves = 0
    for i in range(N):
        if i == 0 or H[i] <= H[i-1]:
            continue
        moves = 0
        while i+moves+1 < N and H[i+moves+1] <= H[i]:
            moves += 1
        max_moves = max(max_moves, moves)
    return max_moves

def main():
    N, H = get_input()
    print(solve(N, H))

if __name__ == '__main__':
    main()

