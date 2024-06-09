
def is_reproducible(art_piece):
    # Initialize a 2D array to store the colors of the art piece
    art_piece_array = []
    for row in art_piece:
        art_piece_array.append([])
        for col in row:
            art_piece_array[-1].append(col)
    
    # Initialize a 2D array to store the colors of the reproduced art piece
    reproduced_art_piece_array = [[0] * len(art_piece_array[0]) for _ in range(len(art_piece_array))]
    
    # Iterate through the art piece array and check if the colors match
    for i in range(len(art_piece_array)):
        for j in range(len(art_piece_array[0])):
            if art_piece_array[i][j] != reproduced_art_piece_array[i][j]:
                return "NO"
    
    return "YES"

def main():
    art_piece = []
    for _ in range(int(input())):
        art_piece.append(input())
    print(is_reproducible(art_piece))

if __name__ == '__main__':
    main()

