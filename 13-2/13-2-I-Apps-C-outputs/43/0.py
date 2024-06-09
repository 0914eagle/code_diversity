
def get_min_nubs(mark):
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    # Count the number of '#' in the mark
    num_hashes = sum(line.count('#') for line in mark)
    # Initialize a set to store the positions of the '#' in the mark
    hash_positions = set()
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                hash_positions.add((i, j))
    # Initialize a set to store the positions of the '#' in the stamp
    stamp_positions = set()
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                stamp_positions.add((i, j))
                # If the stamp is stamped exactly twice, remove the position from the stamp_positions set
                if (i, j) in hash_positions:
                    hash_positions.remove((i, j))
    # Return the minimum number of nubs in the stamp
    return num_hashes - len(stamp_positions)

