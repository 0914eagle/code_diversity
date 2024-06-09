
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

def get_pieces(candles, cuts):
    pieces = []
    for candle in candles:
        if not is_candle_on_cut(candle, cuts):
            pieces.append(candle)
    return pieces

def is_valid_cut(cut, r):
    a, b, c = cut
    return a*a + b*b <= 100*100 and c >= 0 and c <= 20000 and math.sqrt(a*a + b*b) <= r

def is_valid_cuts(cuts, r):
    for cut in cuts:
        if not is_valid_cut(cut, r):
            return False
    return True

def is_valid_candles(candles, r):
    for candle in candles:
        if not 0 <= math.sqrt(candle[0]*candle[0] + candle[1]*candle[1]) < r:
            return False
    return True

def is_valid_input(n, m, r, candles, lines):
    if not 1 <= n <= 50 or not 1 <= m <= 15 or not 1 <= r <= 100:
        return False
    if not is_valid_candles(candles, r) or not is_valid_cuts(lines, r):
        return False
    return True

def f1(n, m, r, candles, lines):
    if not is_valid_input(n, m, r, candles, lines):
        return "no"
    pieces = get_pieces(candles, lines)
    if len(pieces) != n:
        return "no"
    for piece in pieces:
        if not is_candle_on_cut(piece, lines):
            return "no"
    return "yes"

def f2(n, m, r, candles, lines):
    if not is_valid_input(n, m, r, candles, lines):
        return "no"
    pieces = get_pieces(candles, lines)
    if len(pieces) != n:
        return "no"
    for piece in pieces:
        if not is_candle_on_cut(piece, lines):
            return "no"
    return "yes"

if __name__ == '__main__':
    n, m, r, candles, lines = get_input()
    print(f1(n, m, r, candles, lines))

