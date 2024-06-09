
def frame_crossword(puzzle, frame_size):
    u, l, r, d = frame_size
    m, n = len(puzzle), len(puzzle[0])
    framed_puzzle = [['#' for _ in range(l + u + r)] for _ in range(d + u + d)]
    for i in range(d):
        framed_puzzle[i][l:l + n] = puzzle[i]
    for i in range(d, d + m):
        framed_puzzle[i][l:l + n] = puzzle[i - d]
    for i in range(d + m, d + m + d):
        framed_puzzle[i][l:l + n] = puzzle[i - d - m]
    return [''.join(row) for row in framed_puzzle]

