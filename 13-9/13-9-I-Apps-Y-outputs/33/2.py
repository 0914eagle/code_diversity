
def get_input():
    N = int(input())
    H = list(map(int, input().split()))
    return N, H

def solve(N, H):
    max_move = 0
    for i in range(N):
        if i > 0 and H[i] >= H[i-1]:
            continue
        move = 1
        while i+move < N and H[i+move] >= H[i]:
            move += 1
        max_move = max(max_move, move)
    return max_move

def main():
    N, H = get_input()
    print(solve(N, H))

if __name__ == '__main__':
    main()

