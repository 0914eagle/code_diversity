
def can_grasshopper_eat_insect(line, k):
    n = len(line)
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        if line[i] == 'G':
            grid[i][i] = 1
        elif line[i] == 'T':
            grid[i][i] = 2
    
    for i in range(n):
        for j in range(i+1, min(i+k+1, n)):
            if grid[i][j] == 1 and grid[j][i] == 0:
                grid[j][i] = 1
    
    for i in range(n):
        if grid[i][n-1] == 2:
            return "YES"
    
    return "NO"

