
def solve(maps):
    n, m = len(maps[0]), len(maps[1])
    for i in range(n-m+1):
        for j in range(m-m+1):
            if all(maps[0][i:i+m] == maps[1][j:j+m] for maps in maps):
                return i+1, j+1
    return -1, -1

