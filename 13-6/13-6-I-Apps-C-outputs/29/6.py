
def get_input():
    R, C = map(int, input().split())
    maze = [input() for _ in range(R)]
    return R, C, maze

def find_exit(maze, R, C):
    # Initialize variables
    exit_found = False
    time_taken = 0
    queue = [(0, 0)]

    # Loop until the exit is found or the queue is empty
    while not exit_found and queue:
        # Get the current position from the queue
        row, col = queue.pop(0)

        # Check if the current position is the exit
        if maze[row][col] == "J":
            exit_found = True
            break

        # Check if the current position is on fire
        if maze[row][col] == "F":
            time_taken += 1
            continue

        # Add the adjacent positions to the queue
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < R and 0 <= c < C and maze[r][c] != "#":
                queue.append((r, c))

    # Return the time taken to find the exit
    return time_taken if exit_found else -1

def main():
    R, C, maze = get_input()
    print(find_exit(maze, R, C))

if __name__ == '__main__':
    main()

