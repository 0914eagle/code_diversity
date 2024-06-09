
def f1(N, B, x, y):
    # Initialize a 2D array to represent the matrix
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    # Place the bombs in the matrix
    for i in range(B):
        matrix[x[i] - 1][y[i] - 1] += 1

    # Initialize a queue to store the positions of the bombs to be defused
    queue = [(0, 0)]

    # Initialize a set to keep track of the visited cells
    visited = set()

    # Initialize a variable to store the minimum number of moves required
    min_moves = 0

    # Loop until the queue is empty
    while queue:
        # Get the current position from the queue
        x, y = queue.pop(0)

        # If the current position is a corner, defuse the bomb and break
        if x in [0, N - 1] and y in [0, N - 1]:
            matrix[x][y] -= 1
            break

        # If the current position is not visited, mark it as visited and add its neighbors to the queue
        if (x, y) not in visited:
            visited.add((x, y))
            queue.append((x - 1, y))
            queue.append((x + 1, y))
            queue.append((x, y - 1))
            queue.append((x, y + 1))

        # Increment the minimum number of moves required
        min_moves += 1

    # Return the minimum number of moves required
    return min_moves

def f2(...):
    # Implement f2() here
    pass

if __name__ == '__main__':
    N, B = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(f1(N, B, x, y))

