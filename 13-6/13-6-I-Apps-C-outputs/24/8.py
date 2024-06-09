
def read_input():
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    return n, m, mark

def f1(n, m, mark):
    # Initialize a 2D array to keep track of the number of times each cell is marked
    marked_cells = [[0] * m for _ in range(n)]

    # Loop through each cell in the mark and increment the corresponding cell in the marked_cells array
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                marked_cells[i][j] += 1

    # Loop through each row in the marked_cells array and find the maximum number of times a cell is marked
    max_marked = max(map(max, marked_cells))

    # Return the minimum number of nubs that could have possibly made the mark
    return max_marked

def f2(n, m, mark):
    # Initialize a 2D array to keep track of the number of times each cell is marked
    marked_cells = [[0] * m for _ in range(n)]

    # Loop through each cell in the mark and increment the corresponding cell in the marked_cells array
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                marked_cells[i][j] += 1

    # Loop through each row in the marked_cells array and find the maximum number of times a cell is marked
    max_marked = max(map(max, marked_cells))

    # Return the minimum number of nubs that could have possibly made the mark
    return max_marked

if __name__ == '__main__':
    n, m, mark = read_input()
    print(f1(n, m, mark))

