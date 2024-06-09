
def f1(n_r, n_c, n, m, icons):
    # Initialize a 2D array to represent the screen
    screen = [[0 for _ in range(n_c)] for _ in range(n_r)]

    # Populate the screen with the icons
    for i in range(n):
        r, c = icons[i * 2], icons[i * 2 + 1]
        screen[r][c] = 1

    # Initialize a variable to keep track of the minimum number of icons to move
    min_icons = float('inf')

    # Iterate through all possible combinations of icons to move
    for i in range(1, n + 1):
        for combination in itertools.combinations(range(n), i):
            # Check if the combination forms a rectangle
            if is_rectangle(screen, combination):
                # Calculate the number of icons to move
                icons_to_move = n - len(combination)

                # Update the minimum number of icons to move if necessary
                if icons_to_move < min_icons:
                    min_icons = icons_to_move

    return min_icons

def f2(n_r, n_c, n, m, icons):
    # Initialize a 2D array to represent the screen
    screen = [[0 for _ in range(n_c)] for _ in range(n_r)]

    # Populate the screen with the icons
    for i in range(n):
        r, c = icons[i * 2], icons[i * 2 + 1]
        screen[r][c] = 1

    # Initialize a variable to keep track of the minimum number of icons to move
    min_icons = float('inf')

    # Iterate through all possible combinations of icons to move
    for i in range(1, n + 1):
        for combination in itertools.combinations(range(n), i):
            # Check if the combination forms a rectangle
            if is_rectangle(screen, combination):
                # Calculate the number of icons to move
                icons_to_move = n - len(combination)

                # Update the minimum number of icons to move if necessary
                if icons_to_move < min_icons:
                    min_icons = icons_to_move

    return min_icons

def is_rectangle(screen, combination):
    # Initialize a variable to keep track of the number of rows and columns spanned
    rows, cols = 0, 0

    # Iterate through the combination of icons
    for i in combination:
        r, c = icons[i * 2], icons[i * 2 + 1]

        # Update the number of rows and columns spanned
        rows = max(rows, r + 1)
        cols = max(cols, c + 1)

    # Check if the combination forms a rectangle
    return rows == cols

if __name__ == '__main__':
    n_r, n_c, n, m = map(int, input().split())
    icons = [int(x) for x in input().split()]
    print(f1(n_r, n_c, n, m, icons))
    print(f2(n_r, n_c, n, m, icons))

