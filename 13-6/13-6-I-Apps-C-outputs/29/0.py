
def get_input():
    R, C = map(int, input().split())
    maze = [input() for _ in range(R)]
    joe_position = [row.index('J') for row in maze if 'J' in row][0]
    fire_positions = [(row.index('F'), i) for i, row in enumerate(maze) if 'F' in row]
    return R, C, maze, joe_position, fire_positions

def is_safe(maze, joe_position, fire_positions):
    R, C = len(maze), len(maze[0])
    for r, c in fire_positions:
        if r == joe_position[0] and c == joe_position[1]:
            return False
        if r == joe_position[0] and c in range(joe_position[1]-1, joe_position[1]+2):
            return False
        if r in range(joe_position[0]-1, joe_position[0]+2) and c == joe_position[1]:
            return False
    return True

def escape_time(maze, joe_position, fire_positions):
    R, C = len(maze), len(maze[0])
    queue = [(joe_position[0], joe_position[1], 0)]
    visited = set()
    while queue:
        r, c, time = queue.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if r == 0 or c == 0 or r == R-1 or c == C-1:
            return time
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#' and (nr, nc) not in visited:
                queue.append((nr, nc, time+1))
    return -1

def main():
    R, C, maze, joe_position, fire_positions = get_input()
    if not is_safe(maze, joe_position, fire_positions):
        print("IMPOSSIBLE")
    else:
        print(escape_time(maze, joe_position, fire_positions))

if __name__ == '__main__':
    main()

