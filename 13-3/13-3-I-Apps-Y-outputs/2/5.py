
def frame_crossword(crossword, frame_size):
    # Extract the dimensions of the crossword and the frame size
    m, n = len(crossword), len(crossword[0])
    u, l, r, d = frame_size
    
    # Initialize the framed crossword with the appropriate number of # and . characters
    framed_crossword = [['#' for _ in range(u + l + r + n)] for _ in range(d + u + m + n)]
    
    # Fill in the crossword characters in the appropriate positions
    for i in range(m):
        for j in range(n):
            framed_crossword[u + i + 1][l + j + 1] = crossword[i][j]
    
    # Fill in the remaining # and . characters to complete the frame
    for i in range(d + u + m + n):
        for j in range(u + l + r + n):
            if framed_crossword[i][j] == '.':
                framed_crossword[i][j] = '#' if (i + j) % 2 == 0 else '.'
    
    return framed_crossword

