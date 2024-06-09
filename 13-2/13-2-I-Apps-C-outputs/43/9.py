
def get_min_nubs(mark):
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    # Count the number of '#' symbols in the mark
    num_hashes = sum(line.count('#') for line in mark)
    # Initialize a set to store the positions of the '#' symbols
    hash_positions = set()
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                hash_positions.add((i, j))
    # Initialize a set to store the positions of the '#' symbols in the second stamping
    second_stamp_positions = set()
    for i, j in hash_positions:
        if (i, j) in second_stamp_positions:
            continue
        second_stamp_positions.add((i, j))
        for k in range(i, n):
            for l in range(m):
                if mark[k][l] == '#':
                    second_stamp_positions.add((k, l))
                    break
    return num_hashes - len(second_stamp_positions)

