
def f1(H, W, S):
    # Initialize the maximum possible number of moves to 0
    max_moves = 0
    
    # Loop through each possible starting square
    for i in range(H):
        for j in range(W):
            # If the current square is a road square, try to find the shortest path to the goal square
            if S[i][j] == '.':
                # Use BFS to find the shortest path to the goal square
                queue = [(i, j)]
                visited = set()
                while queue:
                    x, y = queue.pop(0)
                    if (x, y) not in visited:
                        visited.add((x, y))
                        if x == H-1 and y == W-1:
                            # If the current square is the goal square, return the number of moves made
                            return len(visited) - 1
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
                                queue.append((nx, ny))
    
    # If no path was found, return the maximum possible number of moves
    return max_moves

def f2(H, W, S):
    # Initialize the maximum possible number of moves to 0
    max_moves = 0
    
    # Loop through each possible starting square
    for i in range(H):
        for j in range(W):
            # If the current square is a road square, try to find the shortest path to the goal square
            if S[i][j] == '.':
                # Use DFS to find the shortest path to the goal square
                stack = [(i, j)]
                visited = set()
                while stack:
                    x, y = stack.pop()
                    if (x, y) not in visited:
                        visited.add((x, y))
                        if x == H-1 and y == W-1:
                            # If the current square is the goal square, return the number of moves made
                            return len(visited) - 1
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
                                stack.append((nx, ny))
    
    # If no path was found, return the maximum possible number of moves
    return max_moves

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    print(max(f1(H, W, S), f2(H, W, S)))

