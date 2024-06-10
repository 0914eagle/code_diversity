
def read_map(grid):
    N, M = len(grid), len(grid[0])
    start, treasure = (0, 0), (0, 0)
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                treasure = (i, j)
    return N, M, start, treasure

def bfs(N, M, start, treasure, K):
    queue = [(start, K)]
    visited = set()
    while queue:
        (i, j), stamina = queue.pop(0)
        if (i, j) == treasure:
            return stamina
        for (ii, jj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < N and 0 <= jj < M and (ii, jj) not in visited and grid[ii][jj] != '#':
                cost = 1 if grid[ii][jj] == '.' else 2 if grid[ii][jj] == 'F' else 3
                if stamina - cost >= 0:
                    queue.append(((ii, jj), stamina - cost))
                    visited.add((ii, jj))
    return -1

def solve(grid, K):
    N, M, start, treasure = read_map(grid)
    return bfs(N, M, start, treasure, K)

if __name__ == '__main__':
    grid = [
        list(input())
        for _ in range(int(input()))
    ]
    K = int(input())
    print(solve(grid, K))

