
def get_min_nubs(mark):
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    # Count the number of '#' symbols in the mark
    num_hashes = sum(line.count('#') for line in mark)
    # Initialize a set to store the positions of the '#' symbols
    hash_positions = set()
    # Iterate over the mark and add the positions of the '#' symbols to the set
    for i, line in enumerate(mark):
        for j, char in enumerate(line):
            if char == '#':
                hash_positions.add((i, j))
    # Initialize a variable to store the minimum number of nubs
    min_nubs = 0
    # Iterate over the hash positions and check if they are part of a horizontal or vertical line
    for i, j in hash_positions:
        # Check if the hash is part of a horizontal line
        if j + 1 in hash_positions and i == hash_positions[j + 1][0]:
            min_nubs += 1
        # Check if the hash is part of a vertical line
        if i + 1 in hash_positions and j == hash_positions[i + 1][1]:
            min_nubs += 1
    return num_hashes - min_nubs

