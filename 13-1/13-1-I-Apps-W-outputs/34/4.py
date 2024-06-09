
import sys

def knight_moves(x, y):
    # Initialize the number of ways to reach (x, y) as 0
    ways = 0

    # Base case: if we are already at (x, y), there is only 1 way to reach there
    if x == y:
        return 1

    # Recursive case: consider all possible moves from (x-1, y-2), (x-2, y-1), (x-2, y+1), and (x-1, y+2)
    for i in range(4):
        # Calculate the next position based on the move
        next_x = x - 1 + 2 * (i // 2)
        next_y = y - 1 + 2 * (i % 2)

        # If the next position is within the bounds of the grid and has not been visited before, mark it as visited and recurse
        if 0 <= next_x <= x and 0 <= next_y <= y and (next_x, next_y) not in visited:
            visited.add((next_x, next_y))
            ways += knight_moves(next_x, next_y)

    return ways

if __name__ == '__main__':
    x, y = map(int, input().split())
    visited = set()
    print(knight_moves(x, y) % (10**9 + 7))

