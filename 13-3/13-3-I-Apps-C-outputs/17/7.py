
def get_valid_colorings(n, a):
    # Initialize a 2D array to store the colorings
    colorings = [[[] for _ in range(n)] for _ in range(n)]

    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(n):
            # If the current cell is not colored, skip it
            if a[i][j] == -1:
                continue

            # If the current cell is colored, check if it forms a valid loop
            if not is_valid_loop(colorings, i, j, a[i][j]):
                return 0

    # If all cells are colored and form valid loops, return 1
    return 1

def is_valid_loop(colorings, i, j, color):
    # If the current cell is not colored, return False
    if color == -1:
        return False

    # If the current cell is colored, check if it forms a valid loop
    if colorings[i][j] == color:
        return True

    # If the current cell is not colored, color it with the current color
    colorings[i][j] = color

    # Check if the current cell is part of a valid loop
    if i > 0 and is_valid_loop(colorings, i-1, j, color):
        return True
    if i < len(colorings) - 1 and is_valid_loop(colorings, i+1, j, color):
        return True
    if j > 0 and is_valid_loop(colorings, i, j-1, color):
        return True
    if j < len(colorings[0]) - 1 and is_valid_loop(colorings, i, j+1, color):
        return True

    # If the current cell is not part of a valid loop, return False
    return False

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

print(get_valid_colorings(n, a))

