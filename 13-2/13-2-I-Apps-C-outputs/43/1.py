
def get_min_nubs(mark):
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    # Count the number of '#' in the mark
    num_hashes = sum(line.count('#') for line in mark)
    # Initialize a set to store the possible number of nubs
    possible_nubs = set()
    # Iterate over the rows of the mark
    for i in range(n):
        # Iterate over the columns of the mark
        for j in range(m):
            # If the current cell is a '#', add the number of '#' in the current row and column to the set of possible nubs
            if mark[i][j] == '#':
                possible_nubs.add(sum(mark[i][:j+1].count('#') for mark in mark[:i+1]))
    # Return the minimum number of possible nubs
    return min(possible_nubs)

