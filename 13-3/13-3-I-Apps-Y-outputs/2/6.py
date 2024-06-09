
def solve(crossword, frame):
    # Initialize variables
    m, n = len(crossword), len(crossword[0])
    u, l, r, d = frame
    result = []

    # Add top frame
    result.append('#' * (2 * l + n))

    # Add left and right frames
    for i in range(m):
        result.append('#' + '.' * l + crossword[i] + '.' * r + '#')

    # Add bottom frame
    result.append('#' * (2 * l + n))

    return '\n'.join(result)

