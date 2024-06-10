
def get_platforms(n, m, c):
    platforms = []
    for i in range(m):
        platforms.append([j for j in range(c[i])])
    return platforms

def can_reach(n, m, d, c, platforms):
    visited = [False] * (n + 2)
    queue = [0]
    visited[0] = True
    while queue:
        curr = queue.pop(0)
        if curr == n + 1:
            return True
        for i in range(m):
            for j in range(c[i]):
                next_cell = curr + j + 1
                if next_cell <= n + 1 and not visited[next_cell] and platforms[i][j] == next_cell:
                    queue.append(next_cell)
                    visited[next_cell] = True
    return False

def move_platforms(n, m, c, platforms):
    for i in range(m):
        for j in range(c[i]):
            platforms[i][j] -= 1
    return platforms

def solve(n, m, d, c):
    platforms = get_platforms(n, m, c)
    while True:
        if can_reach(n, m, d, c, platforms):
            return "YES"
        platforms = move_platforms(n, m, c, platforms)

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print(solve(n, m, d, c))

