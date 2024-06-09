
def frame_crossword(crossword, frame_size):
    # Extract the dimensions of the crossword and frame
    m, n = len(crossword), len(crossword[0])
    u, l, r, d = frame_size
    
    # Initialize the framed crossword with the frame characters
    framed_crossword = [['#' for _ in range(l + u + r)] for _ in range(d + u + d)]
    
    # Fill the inner part of the framed crossword with the crossword
    for i in range(d, d + m):
        for j in range(l, l + n):
            framed_crossword[i][j] = crossword[i - d][j - l]
    
    return framed_crossword

