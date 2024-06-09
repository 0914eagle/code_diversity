
def frame_crossword(crossword, U, L, R, D):
    # Initialize the framed crossword with the given dimensions
    framed_crossword = [["."]*(L+R+2) for _ in range(U+D+2)]

    # Fill the inner part of the framed crossword with the given crossword
    for i in range(U, len(framed_crossword)-D):
        for j in range(L, len(framed_crossword[i])-R):
            framed_crossword[i][j] = crossword[i-U][j-L]

    # Add the # characters to the top, bottom, left, and right sides of the framed crossword
    for i in range(len(framed_crossword)):
        framed_crossword[i][0] = "#"
        framed_crossword[i][-1] = "#"
    for j in range(len(framed_crossword[0])):
        framed_crossword[0][j] = "#"
        framed_crossword[-1][j] = "#"

    return framed_crossword

