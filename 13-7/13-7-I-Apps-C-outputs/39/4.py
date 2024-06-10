
def read_input():
    N, M, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(input()))
    return N, M, K, grid

def find_treasure(N, M, K, grid):
    days = 0
    stamina = K
    start_row, start_col = None, None
    treasure_row, treasure_col = None, None
    
    for row in range(N):
        for col in range(M):
            if grid[row][col] == 'S':
                start_row, start_col = row, col
            elif grid[row][col] == 'G':
                treasure_row, treasure_col = row, col
    
    queue = [(start_row, start_col, 0)]
    
    while queue:
        row, col, day = queue.pop(0)
        
        if row == treasure_row and col == treasure_col:
            return days
        
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < N and 0 <= c < M and grid[r][c] != '#' and (r, c) not in queue:
                queue.append((r, c, day+1))
        
        stamina -= 1
        if stamina == 0:
            stamina = K
            days += 1
    
    return -1

def main():
    N, M, K, grid = read_input()
    print(find_treasure(N, M, K, grid))

if __name__ == '__main__':
    main()

