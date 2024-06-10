
def get_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    return H, W, S

def count_adjacent_bombs(i, j, S):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if 0 <= i+di < len(S) and 0 <= j+dj < len(S[0]) and S[i+di][j+dj] == '#':
                count += 1
    return count

def solve(H, W, S):
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                S[i] = S[i][:j] + str(count_adjacent_bombs(i, j, S)) + S[i][j+1:]
    return S

def main():
    H, W, S = get_input()
    print(*solve(H, W, S), sep='\n')

if __name__ == '__main__':
    main()

