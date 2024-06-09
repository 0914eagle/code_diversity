
def get_min_nubs(mark):
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    # Count the number of '#' symbols in the mark
    num_hashes = sum(line.count('#') for line in mark)
    # Initialize a 2D array to store the number of '#' symbols in each cell
    num_hashes_array = [[0] * m for _ in range(n)]
    # Fill in the 2D array based on the mark
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                num_hashes_array[i][j] = 1
    # Check if the mark can be made by stamping exactly twice
    for i in range(n):
        for j in range(m):
            if num_hashes_array[i][j] != 2:
                return -1
    # Count the number of unique '#' symbols in the mark
    unique_hashes = set()
    for i in range(n):
        for j in range(m):
            unique_hashes.add((i, j))
    return num_hashes - len(unique_hashes)

