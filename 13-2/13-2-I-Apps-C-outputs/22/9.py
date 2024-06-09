
def is_reproducible(art_piece):
    # Initialize a 2D array to store the colors of the art piece
    art_piece_array = []
    for row in art_piece:
        art_piece_array.append([])
        for col in row:
            art_piece_array[-1].append(col)

    # Check if the art piece can be reproduced
    for i in range(len(art_piece_array)):
        for j in range(len(art_piece_array[0])):
            if art_piece_array[i][j] != 'W':
                continue
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if k >= len(art_piece_array) or l >= len(art_piece_array[0]):
                        return "NO"
                    if art_piece_array[k][l] != 'W':
                        return "NO"

    return "YES"

def main():
    art_piece = []
    for _ in range(int(input())):
        art_piece.append(input())
    print(is_reproducible(art_piece))

if __name__ == '__main__':
    main()

