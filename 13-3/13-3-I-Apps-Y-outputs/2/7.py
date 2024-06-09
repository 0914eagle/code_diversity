
def frame_crossword(crossword, frame_size):
    u, l, r, d = frame_size
    m, n = len(crossword), len(crossword[0])
    framed_crossword = [['#' if i % 2 == j % 2 else '.' for i in range(l + m + r)] for j in range(u + n + d)]
    for i in range(m):
        for j in range(n):
            framed_crossword[u + i][l + j] = crossword[i][j]
    return '\n'.join(''.join(row) for row in framed_crossword)

