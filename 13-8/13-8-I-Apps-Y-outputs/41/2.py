
def solve(s):
    H, W = map(int, input().split())
    s = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    q = [(0, 0)]
    while q:
        i, j = q.pop(0)
        if s[i][j] == '#':
            visited[i][j] = True
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < H and 0 <= y < W and not visited[x][y] and s[x][y] == '.':
                    q.append((x, y))
    for i in range(H):
        for j in range(W):
            if s[i][j] == '#' and not visited[i][j]:
                return "No"
    return "Yes"

def main():
    print(solve(input()))

if __name__ == '__main__':
    main()

