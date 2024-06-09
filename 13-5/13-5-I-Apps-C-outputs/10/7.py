
import math

def get_input():
    n, m, r = map(int, input().split())
    candles = []
    for i in range(n):
        x, y = map(int, input().split())
        candles.append((x, y))
    lines = []
    for i in range(m):
        a, b, c = map(int, input().split())
        lines.append((a, b, c))
    return n, m, r, candles, lines

def is_candle_on_line(candle, line):
    a, b, c = line
    x, y = candle
    return a*x + b*y + c == 0

def is_candle_on_cut(candle, cuts):
    for cut in cuts:
        if is_candle_on_line(candle, cut):
            return True
    return False

def is_candle_in_piece(candle, piece):
    x, y = candle
    x1, y1, x2, y2 = piece
    return (x1 <= x <= x2) and (y1 <= y <= y2)

def get_pieces(candles, cuts):
    pieces = []
    for candle in candles:
        if not is_candle_on_cut(candle, cuts):
            continue
        for piece in pieces:
            if is_candle_in_piece(candle, piece):
                break
        else:
            pieces.append((candle[0], candle[1], candle[0], candle[1]))
    return pieces

def is_valid_piece(piece, cuts):
    x1, y1, x2, y2 = piece
    for cut in cuts:
        a, b, c = cut
        if a == 0:
            if b > 0:
                if x1 <= 0 <= x2 and y1 <= 0 <= y2:
                    return False
            elif b < 0:
                if x1 <= 0 <= x2 and y1 >= 0 >= y2:
                    return False
            else:
                continue
        elif a > 0:
            if x1 <= 0 <= x2 and y1 <= c/a <= y2:
                return False
        elif a < 0:
            if x1 <= 0 <= x2 and y1 >= c/a >= y2:
                return False
    return True

def is_valid_pieces(pieces, cuts):
    for piece in pieces:
        if not is_valid_piece(piece, cuts):
            return False
    return True

def is_valid_cuts(cuts, n):
    for cut in cuts:
        if not is_valid_line(cut):
            return False
    return len(cuts) == n

def is_valid_line(line):
    a, b, c = line
    if a == 0 and b == 0:
        return False
    return True

def solve(n, m, r, candles, lines):
    cuts = []
    for line in lines:
        cuts.append(line)
    pieces = get_pieces(candles, cuts)
    if not is_valid_pieces(pieces, cuts):
        return "no"
    if not is_valid_cuts(cuts, n):
        return "no"
    return "yes"

if __name__ == '__main__':
    n, m, r, candles, lines = get_input()
    print(solve(n, m, r, candles, lines))

