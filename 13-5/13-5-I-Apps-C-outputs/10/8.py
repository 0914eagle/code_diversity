
import math

def get_candle_locations(n, r):
    candle_locations = []
    for i in range(n):
        x, y = map(float, input().split())
        candle_locations.append((x, y))
    return candle_locations

def get_cut_lines(m):
    cut_lines = []
    for i in range(m):
        a, b, c = map(float, input().split())
        cut_lines.append((a, b, c))
    return cut_lines

def is_cut_valid(cut_line, candle_locations):
    for candle in candle_locations:
        if cut_line[0] * candle[0] + cut_line[1] * candle[1] + cut_line[2] == 0:
            return False
    return True

def is_piece_valid(piece, candle_locations):
    for candle in candle_locations:
        if piece[0] * candle[0] + piece[1] * candle[1] + piece[2] == 0:
            return False
    return True

def get_pieces(cut_lines, candle_locations):
    pieces = []
    for cut_line in cut_lines:
        piece = []
        for candle in candle_locations:
            if cut_line[0] * candle[0] + cut_line[1] * candle[1] + cut_line[2] < 0:
                piece.append(candle)
        pieces.append(piece)
    return pieces

def is_division_valid(pieces, candle_locations):
    for piece in pieces:
        if len(piece) != 1:
            return False
    return True

def main():
    n, m, r = map(int, input().split())
    candle_locations = get_candle_locations(n, r)
    cut_lines = get_cut_lines(m)
    pieces = get_pieces(cut_lines, candle_locations)
    if is_division_valid(pieces, candle_locations):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()

