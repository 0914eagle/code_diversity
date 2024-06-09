
import math

def get_candle_locations(n):
    candle_locations = []
    for i in range(n):
        x, y = map(int, input().split())
        candle_locations.append((x, y))
    return candle_locations

def get_cut_lines(m):
    cut_lines = []
    for i in range(m):
        a, b, c = map(int, input().split())
        cut_lines.append((a, b, c))
    return cut_lines

def is_candle_on_cut(candle, cut):
    a, b, c = cut
    x, y = candle
    return a*x + b*y + c == 0

def is_cut_valid(cut, candle_locations):
    for candle in candle_locations:
        if is_candle_on_cut(candle, cut):
            return False
    return True

def is_candle_on_cut_line(candle, cut_lines):
    for cut in cut_lines:
        if is_candle_on_cut(candle, cut):
            return True
    return False

def is_candle_on_cut_lines(candle, cut_lines):
    for cut in cut_lines:
        if is_candle_on_cut(candle, cut):
            return True
    return False

def get_candle_pieces(candle_locations, cut_lines):
    candle_pieces = []
    for candle in candle_locations:
        if is_candle_on_cut_lines(candle, cut_lines):
            candle_pieces.append(candle)
    return candle_pieces

def is_candle_piece_valid(candle_piece, candle_locations):
    for candle in candle_locations:
        if candle == candle_piece:
            return True
    return False

def is_candle_piece_count_valid(candle_pieces, candle_locations):
    return len(candle_pieces) == len(candle_locations)

def is_candle_piece_location_valid(candle_pieces, candle_locations):
    for candle_piece in candle_pieces:
        if not is_candle_on_cut_lines(candle_piece, cut_lines):
            return False
    return True

def is_candle_piece_valid(candle_piece, candle_locations):
    return is_candle_piece_count_valid(candle_pieces, candle_locations) and is_candle_piece_location_valid(candle_pieces, candle_locations)

def is_candle_pieces_valid(candle_pieces, candle_locations):
    for candle_piece in candle_pieces:
        if not is_candle_piece_valid(candle_piece, candle_locations):
            return False
    return True

def main():
    n, m, r = map(int, input().split())
    candle_locations = get_candle_locations(n)
    cut_lines = get_cut_lines(m)
    candle_pieces = get_candle_pieces(candle_locations, cut_lines)
    if is_candle_pieces_valid(candle_pieces, candle_locations):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()

