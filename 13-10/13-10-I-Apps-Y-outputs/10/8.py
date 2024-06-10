
def get_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    return H, W, S

def count_bombs(S, i, j):
    bombs = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if 0 <= x < H and 0 <= y < W and S[x][y] == '#':
                bombs += 1
    return bombs

def replace_dots(S):
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                S[i] = S[i][:j] + str(count_bombs(S, i, j)) + S[i][j+1:]
    return S

def main():
    H, W, S = get_input()
    print(*replace_dots(S), sep='\n')

if __name__ == '__main__':
    main()

