
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

def check_rectangles(table):
    def dfs(i, j, val):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or table[i][j] != val:
            return
        visited[i][j] = True
        dfs(i+1, j, val)
        dfs(i-1, j, val)
        dfs(i, j+1, val)
        dfs(i, j-1, val)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    rectangles = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(i, j, table[i][j])
                rectangles += 1
    return rectangles

if check_rectangles(table) > k:
    print(-1)
else:
    print(max(0, check_rectangles(table) - 1))
