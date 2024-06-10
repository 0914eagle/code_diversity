
def get_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    return H, W, S

def get_adjacent_bombs(S, i, j):
    H, W = len(S), len(S[0])
    adjacent_bombs = 0
    for k in range(max(i-1, 0), min(i+2, H)):
        for l in range(max(j-1, 0), min(j+2, W)):
            if S[k][l] == '#':
                adjacent_bombs += 1
    return adjacent_bombs

def replace_empties(S):
    H, W = len(S), len(S[0])
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                S[i] = S[i][:j] + str(get_adjacent_bombs(S, i, j)) + S[i][j+1:]
    return S

def main():
    H, W, S = get_input()
    print(*replace_empties(S), sep='\n')

if __name__ == '__main__':
    main()

