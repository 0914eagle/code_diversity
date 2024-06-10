
def get_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    return H, W, S

def count_adjacent_bombs(H, W, S):
    adjacent_bombs = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if 0 <= k < H and 0 <= l < W and S[k][l] == '#':
                            adjacent_bombs[i][j] += 1
    return adjacent_bombs

def print_output(H, W, S, adjacent_bombs):
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                S[i] = S[i][:j] + str(adjacent_bombs[i][j]) + S[i][j+1:]
        print(S[i])

if __name__ == '__main__':
    H, W, S = get_input()
    adjacent_bombs = count_adjacent_bombs(H, W, S)
    print_output(H, W, S, adjacent_bombs)

