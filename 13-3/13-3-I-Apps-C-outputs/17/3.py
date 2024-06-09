
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
    if colorings[i][j] != [] and colorings[i][j][0] != color:
        return False

    # If the current cell is colored and forms a valid loop, return True
    return True

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print(get_valid_colorings(n, a))

