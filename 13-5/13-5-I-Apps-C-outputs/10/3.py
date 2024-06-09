
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

def is_cut_valid(cut_line, candle_location):
    a, b, c = cut_line
    x, y = candle_location
    return a*x + b*y + c == 0

def is_piece_valid(piece, candle_locations):
    for candle_location in candle_locations:
        if not is_cut_valid(piece, candle_location):
            return False
    return True

def f1(n, m, r):
    candle_locations = get_candle_locations(n)
    cut_lines = get_cut_lines(m)
    for candle_location in candle_locations:
        piece = []
        for cut_line in cut_lines:
            if is_cut_valid(cut_line, candle_location):
                piece.append(cut_line)
        if not is_piece_valid(piece, candle_locations):
            return "no"
    return "yes"

def f2(n, m, r):
    candle_locations = get_candle_locations(n)
    cut_lines = get_cut_lines(m)
    for cut_line in cut_lines:
        piece = []
        for candle_location in candle_locations:
            if is_cut_valid(cut_line, candle_location):
                piece.append(candle_location)
        if not is_piece_valid(piece, candle_locations):
            return "no"
    return "yes"

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    print(f1(n, m, r))
    print(f2(n, m, r))

