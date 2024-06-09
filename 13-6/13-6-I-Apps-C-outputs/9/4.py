
def f1(n_r, n_c, n, m, files):
    # Initialize a 2D array to represent the screen
    screen = [[0 for _ in range(n_c)] for _ in range(n_r)]

    # Place the files on the screen
    for i in range(n):
        r, c = files[i * 2], files[i * 2 + 1]
        screen[r][c] = 1

    # Initialize a variable to store the minimum number of files to move
    min_files_to_move = float('inf')

    # Iterate through all possible positions of the files to be deleted
    for i in range(n_r):
        for j in range(n_c):
            # Check if the current position is valid for the files to be deleted
            if screen[i][j] == 0:
                continue

            # Initialize a variable to store the number of files moved
            files_moved = 0

            # Iterate through all files to be deleted
            for k in range(n):
                # Check if the current file is at the current position
                if screen[i][j] == 1:
                    # Increment the number of files moved
                    files_moved += 1

                    # Set the current position to 0
                    screen[i][j] = 0

            # Check if the current position is a valid position for the files to be deleted
            if files_moved == n:
                # Update the minimum number of files to move
                min_files_to_move = min(min_files_to_move, files_moved)

    return min_files_to_move

def f2(n_r, n_c, n, m, files):
    # Initialize a 2D array to represent the screen
    screen = [[0 for _ in range(n_c)] for _ in range(n_r)]

    # Place the files on the screen
    for i in range(n):
        r, c = files[i * 2], files[i * 2 + 1]
        screen[r][c] = 1

    # Initialize a variable to store the minimum number of files to move
    min_files_to_move = float('inf')

    # Iterate through all possible positions of the files to be deleted
    for i in range(n_r):
        for j in range(n_c):
            # Check if the current position is valid for the files to be deleted
            if screen[i][j] == 0:
                continue

            # Initialize a variable to store the number of files moved
            files_moved = 0

            # Iterate through all files to be deleted
            for k in range(n):
                # Check if the current file is at the current position
                if screen[i][j] == 1:
                    # Increment the number of files moved
                    files_moved += 1

                    # Set the current position to 0
                    screen[i][j] = 0

            # Check if the current position is a valid position for the files to be deleted
            if files_moved == n:
                # Update the minimum number of files to move
                min_files_to_move = min(min_files_to_move, files_moved)

    return min_files_to_move

if __name__ == '__main__':
    n_r, n_c, n, m = map(int, input().split())
    files = [int(x) for x in input().split()]
    print(f1(n_r, n_c, n, m, files))
    print(f2(n_r, n_c, n, m, files))

